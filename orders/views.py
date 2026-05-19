from django.shortcuts import render, redirect
from carts.models import CartItem
from .models import Address, Order, OrderItem,Products
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def checkout(request,product_id=None):
    if product_id:

        product = Products.objects.get(id=product_id)

        checkout_items = [
            {
                "product": product,
                "quantity": 1
            }
        ]

        total = product.price

    else:
        checkout_items = CartItem.objects.filter(user=request.user)
        total = 0

        for item in checkout_items:
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

        for item in checkout_items:
            if not product_id:

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )
            else:

                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["product"].price,
                )
            
            if not product_id:
                checkout_items.delete()
        
            return redirect('orders_success')

    return render(request, "orders/checkout.html", {'cart_items': checkout_items,'total': total})

@login_required
def orders_success(request):
    return render(request,'orders/orders_success.html')


@login_required
def orders(request):
    orders=Order.objects.filter(
        user=request.user
    ).order_by('-created_at')
    return render(request,'orders/orders.html',{'orders':orders})

@login_required
def delete_order(request,order_id):
    product=get_object_or_404(Order,id=order_id,user=request.user)
    product.delete()
    return redirect('orders')
