from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    objects = models.Manager()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    objects = models.Manager()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'ProductName {}- User {}- Quantity {}'.format(self.product.name, self.user.username, self.quantity)
