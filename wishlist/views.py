from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Wishlist
from products.models import Products

def add_to_wishlist(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first!")
        return redirect("login")

    product = get_object_or_404(Products, id=id)

    already = Wishlist.objects.filter(user=request.user, product=product).exists()

    if already:
        messages.info(request, "Already in wishlist")
    else:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, "Added to wishlist!")

    return redirect("product_details", id=id)

def wishlist(request):
    return render(request,'wishlist/wishlist.html')

