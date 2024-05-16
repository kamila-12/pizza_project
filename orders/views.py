from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart
 
 
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, pizza=item['pizza'], price=item['price'],
                                         quantity=item['quantity'])
                                        
            cart.clear()
            
            return render(request,
                          'orders/order/ended_order.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create_order.html',
                  {'cart': cart, 'form': form})
 
# def order_pizza(request):
#     cart = Cart(request)
    
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order, product=item['pizza'], price=item['price'], quantity=item['quantity'])
                                   
#             cart.clear()
#     return render(request, 'orders/order/created.html', {'order': order})
#     else:
#         form = OrderCreateForm()
#     return render(request,  'orders/orders/create_order.html', {'cart': cart, 'form': form})
                       

        
                                
                                


# def confirm_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request, 'orders/confirm_order.html', {'order': order})   
