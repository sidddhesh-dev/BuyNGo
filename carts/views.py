from django.shortcuts import render, redirect
from .models import CartItem
from products.models import Products


def add_to_cart(request, product_id):

    product = Products.objects.get(id=product_id)

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    cart_item, created = CartItem.objects.get_or_create(
        session_key=session_key,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_page")


def cart_page(request):

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    items = CartItem.objects.filter(session_key=session_key)

    return render(request, "carts/cart.html", {"items": items})