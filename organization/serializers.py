# serializers.py
from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "description",
            "profile",
            "date_added",
        ]
        read_only_fields = [
            "id",
            "date_added",
        ]  # These fields should not be modified via API
