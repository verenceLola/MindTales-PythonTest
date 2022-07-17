from django.db import models
from .menu import Menu


class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu_item")

    class Meta:
        db_table = "Restaurant"

    def __str__(self):
        return self.name
