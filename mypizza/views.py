from django.shortcuts import render, get_object_or_404
from .models import Pizza
from django.views.generic import ListView, DetailView
from cart.forms import CartAddProductForm

def pizza_detail(request, id):
    pizza = get_object_or_404(Pizza, id=id, available=True)
    
    cart_product_form = CartAddProductForm()
    return render(request, 'mypizza/mypizza/pizza_detail.html', {'product': pizza, 'cart_product_form': cart_product_form})

class PizzaListView(ListView):
    model = Pizza
    template_name = 'mypizza/pizza_list.html'
    
    
    
class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'mypizza/pizza_detail.html'
   
    
# def form_valid(self, form):
#         form.instance.user = self.request.user  
#         return super().form_valid(form)
    
    

