from rest_framework import serializers

from menu.models import Restaurant
from .menu_item import MenuItemSerializer


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    """
    Restaurant Model Serializer
    """

    menu = MenuItemSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ("url", "name", "created_at", "updated_at", "menu")
        read_only_fields = ("created_at", "updated_at")
