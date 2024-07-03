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
        read_only_fields = [
            "date_added",
        ]

    def create(self, validated_data):
        event = validated_data["event"]
        user = validated_data["user"]

        e = Event.objects.get(id=event.id)
        update_event = e

        # Check if the user already liked this event
        existing_like = EventLike.objects.filter(event=event, user=user).first()
        if existing_like:
            # If like already exists, delete it
            existing_like.delete()
            # Decrease likes count of the event
            update_event.likes -= 1
            update_event.save()
        else:
            # If like doesn't exist, create a new one
            new_like = EventLike.objects.create(**validated_data)
            # Increase likes count of the event
            update_event.likes += 1
            update_event.save()
            return new_like

        # Return existing_like if it was deleted
        return existing_like
