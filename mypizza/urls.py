from django.urls import path
from .views import PizzaListView, PizzaDetailView

app_name = 'mypizza'
urlpatterns = [
    path('',  PizzaListView.as_view(), name='pizza_list'),
    path ('pizza/<int:pk>/', PizzaDetailView.as_view(), name='pizza_detail')
  
]