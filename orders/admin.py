from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','order_number','date_created']
	search_fields = ['id','order_number','date_created']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['id']
