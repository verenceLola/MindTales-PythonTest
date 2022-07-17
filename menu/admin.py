from django.contrib import admin
from menu.models import Restaurant, Menu, FoodItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    pass
