from django.urls import path
from .views import order_pizza, confirm_order

app_name = 'orders'

urlpatterns = [
    path('pizza/<int:pizza_id>', order_pizza, name='order_pizza'),
    path('pizza/<int:order_id>/confirm/', confirm_order, name='confirm_order'),
]
