from rest_framework import serializers

from menu.models import FoodItem


class FoodItemSerializer(serializers.ModelSerializer):
    """
    serlizer for the food item model
    """

    class Meta:
        model = FoodItem
        fields = ("name", "meal")
