from rest_framework import serializers

# from organization.serializers import OrganizationSerializer
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    # organization = OrganizationSerializer()

    class Meta:
        model = Story
        fields = [
            "id",
            "organization",
            "hex_code",
            "text",
            "media",
            "date_added",
            "date_of_expiry",
        ]
        read_only_fields = ["id", "date_added", "date_of_expiry"]
