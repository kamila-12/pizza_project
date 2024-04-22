from django.shortcuts import render
from .models import Pizza
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PizzaListView(LoginRequiredMixin, ListView):
    model = Pizza
    template_name = 'mypizza/pizza_list.html'
    
    
    
class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'mypizza/pizza_detail.html'
   
    
# def form_valid(self, form):
#         form.instance.user = self.request.user  
#         return super().form_valid(form)
    
    

