from django.shortcuts import render, redirect
from carts.models import CartItem
from .models import Address, Order, OrderItem
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(
        session_key=session_key
    )

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity


    if request.method == "POST":

        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address_line1 = request.POST.get('address_line1')
        address_line2 = request.POST.get('address_line2')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        state = request.POST.get('state')
        country = request.POST.get('country')

        payment_method = request.POST.get('payment_method')

        address = Address.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            postal_code=postal_code,
            state=state,
            country=country,
        )
        order = Order.objects.create(
            user=request.user,
            address=address,
            total_amount=total,
            payment_method=payment_method,
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )


        cart_items.delete()
        return redirect('orders_success')
    return render(request, "orders/checkout.html", {'cart_items': cart_items,'total': total})

def orders(request):
    return render(request,'orders/orders_success.html')
