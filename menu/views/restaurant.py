from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from menu.models import Restaurant
from menu.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    """
    restaurant model viewset
    """

    queryset = Restaurant.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RestaurantSerializer
