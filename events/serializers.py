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

    def create(self, validated_data):
        event = validated_data["event"]
        user = validated_data["user"]

        # Check if the user already liked this event
        existing_like = EventLike.objects.filter(event=event, user=user).first()
        if existing_like:
            # If like already exists, delete it
            existing_like.delete()
            # Decrease likes count of the event
            event.likes -= 1
            event.save()
        else:
            # If like doesn't exist, create a new one
            new_like = EventLike.objects.create(**validated_data)
            # Increase likes count of the event
            event.likes += 1
            event.save()
            return new_like

        # Return existing_like if it was deleted
        return existing_like
