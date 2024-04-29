from django.db import models
from orders.models import Order

class Delivery(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'В ожидании'),
        ('Confirmed', 'Подтвержден'),
        ('Cancelled', 'Отменен'),
        ('Completed', 'Завершен'),
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    estimated_delivery_time = models.DateTimeField()
