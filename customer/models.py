from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(unique=True)
    address = models.TextField(max_length=1000)
    
def __str__(self):
        return self.name
    