from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from .forms import OrderForm
from .models import Order
from .models import Pizza
 
 
def order_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print('12314')
        
        ###
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
          
            order.total_amount = pizza.price
            order.save()
        ###
          
            if order.id:
                return redirect('orders:confirm_order', order_id=order.id)
            else:
             
                raise Http404("Order could not be created.")
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form, 'pizza': pizza})


def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/confirm_order.html', {'order': order})   
