from django.shortcuts import render
from .models import Pizza
from django.views.generic import ListView, DetailView, CreateView

class PizzaListView(ListView):
    model = Pizza
    template_name = 'mypizza/pizza_list.html'
    
    
    
class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'mypizza/pizza_detail.html'
   
class PizzaCreateView(CreateView):
    model = Pizza
    fields = ['title', 'price', 'image', 'size_pizza', 'ingredients']
    template_name = 'mypizza/pizza_edit.html'
    success_url = '/'
    
# def form_valid(self, form):
#         form.instance.user = self.request.user  
#         return super().form_valid(form)
    
    

