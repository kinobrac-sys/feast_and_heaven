from django.contrib import admin

# Register your models here.
from .models import Dish, LastStep, Shopcart
admin.site.register(Dish)
admin.site.register(Shopcart)
admin.site.register(LastStep)