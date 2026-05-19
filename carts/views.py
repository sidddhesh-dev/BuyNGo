from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Products
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Products,
        id=product_id
    )
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart_page")

@login_required
def cart_page(request):
    items = CartItem.objects.filter(user=request.user)
    total = 0
    for item in items:
        total += item.product.price * item.quantity
    return render(request,"carts/cart.html",{"items": items,"total": total})