from rest_framework import serializers
from menu.models import Menu
from .food_item import FoodItemSerializer


class MenuItemSerializer(serializers.ModelSerializer):
    food = FoodItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = ("name", "created_at", "updated_at", "food")
        read_only_fields = ("created_at", "updated_at")
