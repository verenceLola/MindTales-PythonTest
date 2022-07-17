from django.db import models


class Meal(models.TextChoices):
    """
    meal choices
    """

    Breakfast = "BF"
    Lunch = "L"
    Dinner = "D"


class Menu(models.Model):
    meal = models.CharField(choices=Meal.choices, max_length=50, default=Meal.Lunch)
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "MenuItem"
