from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PizzaListView, PizzaDetailView


urlpatterns = [
    path('',  login_required(PizzaListView.as_view()), name='pizza_list'),
    path ('pizza/<int:pk>/', PizzaDetailView.as_view(), name='pizza_detail')
  
]