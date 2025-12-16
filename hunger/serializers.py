from rest_framework import serializers
from .models import Dish, Shopcart
class HungerSerializer(serializers.Serializer):
    class Meta:
        model = Dish
        fields = '__all__'