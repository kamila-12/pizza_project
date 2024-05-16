from django.db import models
from django.urls import reverse

class Pizza(models.Model): 
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    size_pizza = models.IntegerField(default=0)
    ingredients = models.TextField(null=True)
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['title']),
        
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mypizza:pizza_detail',
                       args=[self.id])

