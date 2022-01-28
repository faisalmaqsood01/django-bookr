from django.urls import path
from auth.views import (
    RegisterView)

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

app_name = 'auth'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
