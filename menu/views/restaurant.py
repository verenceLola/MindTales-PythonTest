from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action

from menu.models import Restaurant
from menu.serializers import RestaurantSerializer

VOTE_DIRECTIONS = (("up", 1), ("down", -1), ("clear", 0))


class RestaurantViewSet(ModelViewSet):
    """
    restaurant model viewset
    """

    queryset = Restaurant.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RestaurantSerializer

    @action(detail=True, methods=["POST"], name="Vote Menu")
    def vote_menu(self, request, pk=None):
        """
        upvote or downvote a restraurant's menu item
        """
        restaurant = self.get_object()

        Restaurant.objects.record_vote(
            restaurant, request.user, request.data.get("vote")
        )
