from django.db import models
from .food_item import FoodItem


class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    food = models.ManyToManyField(FoodItem)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "MenuItem"
