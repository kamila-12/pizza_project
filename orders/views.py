from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import OrderForm
from .models import Order
from .models import Pizza

class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'mypizza/pizza_detail.html'
    
def order_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.total_amount = pizza.price
            order.save()
            return redirect('confirm_order', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form, 'pizza': pizza})

def confirm_order(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/confirm_order.html', {'order': order})