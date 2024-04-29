from django.urls import path
from . import views
from .views import order_pizza, confirm_order

app_name = 'orders'

urlpatterns = [
    path('<int:pizza_id>/', order_pizza, name='order_pizza'),
    path('<int:order_id>/confirm/', views.confirm_order, name='confirm_order'),
]
