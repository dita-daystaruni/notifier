from rest_framework import serializers
from .models import Event, EventLike


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

        # Make all fields read only by default since
        # django admin will handle crud operations on
        # events
        read_only_fields = [
            "__all__",
        ]


class EventLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLike
        fields = "__all__"
