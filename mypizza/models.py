from django.db import models

class Pizza(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images')
    size_pizza = models.IntegerField(default=0)
    ingredients = models.TextField(null=True)

    def __str__(self):
        return self.title

