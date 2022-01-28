# django-bookr
Django Auth + GraphQL Implementation

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/faisalmaqsood01/django-bookr.git
$ cd django-bookr
```


Activate a virtual environment and install dependencies:

```sh
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt

Copy the .env file into your config folder and run the server using cmd
```sh
(env)$ python manage.py runserver


## Django APIS

# Register User.
URL: http://127.0.0.1:8000/v1/auth/register/

Method: Post

payload.
{
    "username": "Faisal",
    "password1": "password123!",
    "password2": "password123!",
    "email": "abc@abc.com",
    "first_name": "Faisal",
    "last_name": "Maqsood"
}

# Login-API

URL: http://127.0.0.1:8000/v1/auth/login
Method: Post
payload
    {
    "username": "Faisal",
    "password": "password123!"
    }


# Get Producs API
URL: http://127.0.0.1:8000/v1/api/products/
Method: GET

