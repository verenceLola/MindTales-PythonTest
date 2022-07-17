from rest_framework import serializers
from menu.models import Menu
from .food_item import FoodItemSerializer
from django.db.models import Count, Q


class MenuItemSerializer(serializers.ModelSerializer):
    food = FoodItemSerializer(many=True)
    votes = serializers.SerializerMethodField(method_name="get_votes", read_only=True)

    def get_votes(self, instance):
        menu_votes = (
            Menu.objects.filter(pk=instance.pk)
            .annotate(
                upvotes=Count("votes", filter=Q(votes__vote=1)),
                downvotes=Count("votes", filter=Q(votes__vote=-1)),
            )
            .prefetch_related()
            .get()
        )

        return {"upvotes": menu_votes.upvotes, "downvotes": menu_votes.downvotes}

    class Meta:
        model = Menu
        fields = ("id", "name", "created_at", "updated_at", "food", "votes")
        read_only_fields = ("created_at", "updated_at")
