from django.shortcuts import render
from carts.models import CartItem

def checkout(request):

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    items = CartItem.objects.filter(session_key=session_key)

    return render(request,"orders/checkout.html",{"items":items})
