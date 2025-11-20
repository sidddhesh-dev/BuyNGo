from django.shortcuts import render
from . import views

def add_cart(request):
    return render(request,'carts/carts.html')
