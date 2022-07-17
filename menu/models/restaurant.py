from django.db import models
from .menu import Menu

from menu.managers import RestaurantManager


class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    menu = models.ManyToManyField(Menu)

    objects = RestaurantManager()

    class Meta:
        db_table = "Restaurant"

    def __str__(self):
        return self.name
