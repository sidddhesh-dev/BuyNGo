from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Products
from .api_services import fetch_data
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def product_list(request):

    category = request.GET.get('category')

    products = Products.objects.all().order_by('-id')

    if category:
        products = products.filter(category__iexact=category)

    # PAGINATION
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'products/products.html', {
        'page_obj': page_obj,
    })

# def product_list(request):
#     products = Products.objects.all()
#     return render(request, 'products/products.html', {"products": products})

@login_required
def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'products/product_details.html', {"product": product})


def import_products(request):
    fetch_data()
    return redirect('product_list')

def search_products(request):
    query = request.GET.get('q', '').strip()

    if query:
        products = Products.objects.filter(name__icontains=query)[:5]
        results = list(products.values('id', 'name'))
        return JsonResponse(results, safe=False)

    return JsonResponse([], safe=False)


@login_required
def buy_now(request, id):
    product = get_object_or_404(Products, id=id)
    context = {"product": product}
    return render(request, "orders/checkout.html", context)
