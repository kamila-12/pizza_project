from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm
from mypizza.models import Pizza
from cart.cart import Cart

@require_POST
def cart_add(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    cart.add(pizza=pizza)
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, pizza_id):
    cart = Cart(request)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    cart.remove(pizza)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    print(f"Cart content: {cart.cart}")
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'cart/cart_detail.html', {'cart': cart})

