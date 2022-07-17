from rest_framework import serializers

from menu.models import Restaurant, Menu, FoodItem
from .menu_item import MenuItemSerializer


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    """
    Restaurant Model Serializer
    """

    menu = MenuItemSerializer(many=True)

    def update(self, instance, validated_data):
        for menu_item in validated_data["menu"]:
            (menu, _) = Menu.objects.get_or_create(
                name=menu_item["name"],
            )

            food_list = []

            for food_item in menu_item["food"]:
                (food, created) = FoodItem.objects.get_or_create(
                    name=food_item["name"], meal=food_item["meal"]
                )
                food_list.append(food)

            menu.food.set(food_list)

        instance.menu.add(menu)

        return instance

    class Meta:
        model = Restaurant
        fields = ("url", "id", "name", "created_at", "updated_at", "menu")
        read_only_fields = ("created_at", "updated_at")
