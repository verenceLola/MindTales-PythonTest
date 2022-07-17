from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth import get_user_model

from menu.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EmployeeSerializer
    queryset = get_user_model().objects.filter(is_active=True).order_by("username")
