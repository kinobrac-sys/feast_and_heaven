from django.contrib import admin

# Register your models here.
from .models import Dish, Order, Shopcart, OrderItem  
admin.site.register(Dish)
admin.site.register(Shopcart)
admin.site.register(Order)
admin.site.register(OrderItem)
#admin.site.register(LastStep)