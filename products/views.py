from django.shortcuts import render,redirect,get_object_or_404
from .models import Products
from .api_services import fetch_data



def product_list(request):
    products = Products.objects.all()
    return render(request, 'products/products.html', {"products": products})


def product_details(request,id):
    product = get_object_or_404(Products, id=id)
    return render(request,'products/product_details.html',{"product": product})

def import_products(request):
    fetch_data()  # fetch and insert products
    return redirect('product_list')

