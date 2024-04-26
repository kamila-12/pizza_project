from django.db import models
from mypizza.models import Pizza
from phonenumber_field.modelfields import PhoneNumberField

class Order(models.Model):
    
    STATUS_CHOICES = (
        ('Pending', 'В пути'),
        ('Confirmed', 'Подтвержден'),
        ('Cancelled', 'Отменен'),
        ('Delivered', 'Доставлен'),
    ) 

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(unique=True)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.pizza.title}"

