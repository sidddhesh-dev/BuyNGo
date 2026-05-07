from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.user_register,name='register'),
    path("login/", views.user_login,name='login'),
    path('account/', views.account_user, name='account'),
    path('logout/',views.logout_user,name="logout")
]
