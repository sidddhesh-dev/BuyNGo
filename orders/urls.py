from django.urls import path
from . import views

urlpatterns = [

    path("checkout/", views.checkout, name="checkout"),
    path('orders_success/',views.orders_success,name='orders_success'),
    path('orders/',views.orders,name='orders')

]