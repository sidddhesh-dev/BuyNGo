from django.urls import path
from . import views

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView
from . import views

urlpatterns = [
    path("register/", views.user_register,name='register'),
    path("login/", views.user_login,name='login'),

    path('accounts/', views.accounts, name='accounts')
]
