from rest_framework.test import APITestCase
from django.urls import reverse
import json
from django.contrib.auth.models import User


class InvalidUserRegistrationApiViewTest(APITestCase):
	url = reverse('auth:auth_register')

	def test_with_invalid_password(self):
		user_data = {
			"username": 'faisal',
			'email': 'abc@example.com',
			'password1': 'password123',
			'password2': 'password321',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
		self.assertTrue("password1" in json.loads(response.content))

	def test_when_username_exist(self):
		user_data1 = {
			"username": 'new_user',
			'email': 'abc@example.com',
			'password1': 'Password123!',
			'password2': 'Password123!',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data1)
		self.assertEqual(201, response.status_code)
		user_data2 = {
			"username": 'new_user',
			'email': 'abc@example.com',
			'password1': 'Password123!',
			'password2': 'Password123!',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data2)
		self.assertEqual(400, response.status_code)

	def test_with_empty_username(self):
		user_data = {
			"username": '',
			'email': 'faisal@example.com',
			'password1': 'testus',
			'password2': 'testus',
			'first_name': "",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)


class UserLoginApiViewTest(APITestCase):
	url = reverse('auth:auth_login')

	def setUp(self):
		self.username = 'faisal'
		self.email = 'faisal@example.com'
		self.password = 'Password123!'
		self.user = User.objects.create_user(self.username, self.email, self.password)
	
	def test_login_without_password_return_bad_request(self):
		response = self.client.post(self.url, {"username": self.username})
		self.assertEqual(400, response.status_code)

	def test_login_with_wrong_password_return_bad_request(self):
		response = self.client.post(self.url, {"username": self.username, 'password': "wrong_password"})
		self.assertEqual(401, response.status_code)

	def test_login_with_valid_data_successful(self):
		response = self.client.post(self.url, {"username": self.username, "password": self.password})
		self.assertEqual(200, response.status_code)
		self.assertTrue("access" in json.loads(response.content))

