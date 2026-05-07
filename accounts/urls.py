from django.urls import path
from . import views

from django.urls import path
from .views import views
from . import views

urlpatterns = [
    path("register/", views.user_register,name='register'),
    path("login/", views.user_login,name='login'),
    path('accounts/', views.accounts, name='accounts')
]
