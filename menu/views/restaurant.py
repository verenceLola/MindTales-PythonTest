from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from rest_framework.decorators import action

from menu.models import Restaurant, Menu
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
        upvote or downvote a restaurant's menu item
        """
        menu_id = request.data.get("menu_id")
        vote = request.data.get("vote")

        result = None

        if not menu_id:
            return response.Response(
                {"error": "Missing menu_id data"}, status=status.HTTP_400_BAD_REQUEST
            )

        if vote is None:
            return response.Response(
                {"error": "Missing vote data"}, status=status.HTTP_400_BAD_REQUEST
            )

        menu_item = self.get_object().menu.get(pk=menu_id)

        try:
            Menu.objects.record_vote(menu_item, request.user, request.data.get("vote"))
            result = response.Response({"detail": "vote recorded"})
        except ValueError:
            result = response.Response(
                {"error": "Invalid vote (must be 1/0/-1)"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return result
