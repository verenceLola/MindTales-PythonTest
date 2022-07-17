from django.db import models
from .food_item import FoodItem
from .vote import Vote
from menu.managers import MenuManager


class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    food = models.ManyToManyField(FoodItem)
    votes = models.ManyToManyField(Vote)

    objects = MenuManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "MenuItem"
