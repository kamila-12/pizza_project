from django.shortcuts import render
from .models import Pizza
from django.views.generic import ListView

class PizzaListView(ListView):
    model = Pizza
    template_name = 'mypizza/pizza_list.html'



