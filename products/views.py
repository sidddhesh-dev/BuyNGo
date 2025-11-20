from django.shortcuts import render
from .models import Products

def product_list(request):
    product=Products.objects.all()
    return render(request, 'products/products.html',{"products":product})