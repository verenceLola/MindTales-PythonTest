from django.db import models


class Meal(models.TextChoices):
    """
    meal choices
    """

    Breakfast = "Breakfast"
    Lunch = "Lunch"
    Dinner = "Dinner"


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    meal = models.CharField(choices=Meal.choices, max_length=50, default=Meal.Lunch)

    def __str__(self):
        return self.name
