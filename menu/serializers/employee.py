from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer for the employees based on the user model
    """

    class Meta:
        model = User
        fields = ("url", "username", "email", "first_name", "last_name")
        read_only_fields = ("url", "username", "email", "first_name", "last_name")
