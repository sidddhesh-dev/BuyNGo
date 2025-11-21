from django.shortcuts import render
from .models import Products
from django.shortcuts import get_object_or_404

def product_list(request):
    product=Products.objects.all()
    return render(request, 'products/products.html',{"products":product})

def product_details(request,id):
    product = get_object_or_404(Products, id=id)
    return render(request,'products/product_details.html',{"product": product})