from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Products
from .api_services import fetch_data


def product_list(request):
    products = Products.objects.all()
    return render(request, 'products/products.html', {"products": products})


def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'products/product_details.html', {"product": product})


def import_products(request):
    fetch_data()
    return redirect('product_list')

def search_products(request):
    query = request.GET.get('q')

    if query:
        products = Products.objects.filter(name__icontains=query)[:5]
        results = list(products.values('id', 'name'))
        return JsonResponse(results, safe=False)

    return JsonResponse([], safe=False)
