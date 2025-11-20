from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.add_cart, name='carts'),
]