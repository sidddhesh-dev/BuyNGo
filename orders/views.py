from django.shortcuts import render
from carts.models import CartItem

def checkout(request):
    return render(request,"orders/checkout.html")

def orders(request):
    return render(request,'orders/orders.html')
