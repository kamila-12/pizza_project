from django.contrib import admin
from .models import Order, OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['pizza']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number',
    'address', 'status',  'created', 'updated', 'paid'
   ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


