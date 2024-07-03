from django.db import OperationalError
from django.utils import timezone
from django.views.generic.edit import CreateView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from events.models import Event, EventLike
from events.serializers import EventLikeSerializer, EventSerializer


# Create your views here.
class ListDueEvents(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(
        start_date__lt=timezone.now(), end_date__gt=timezone.now()
    ).order_by("-likes", "-date_added")


class ListAllEvents(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by("-likes")


class RetrieveEventByID(RetrieveAPIView):
    """Retrieve an event specified by ID"""

    serializer_class = EventSerializer

    try:
        queryset = Event.objects.first()
    except OperationalError as oe:
        pass

    lookup_url_kwarg = "id"


class RetrieveEventByName(RetrieveAPIView):
    """Retrieve an event specified by ID"""

    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = "name"


class LikeEventView(CreateAPIView):
    """Like an event"""

    serializer_class = EventLikeSerializer
    queryset = EventLike.objects.all()

    def post(self, request, *args, **kwargs):
        """I dont know wtf im doing"""
        event = request.data.get("event")
        user = request.data.get("user")

        prisca = Event.objects.get(id=event)
        print(prisca.id, prisca.description, prisca.name, prisca.likes)
        print(prisca)

        # Check if the user already liked this event
        existing_like = EventLike.objects.filter(event=event, user=user).first()
        likes = prisca.likes
        print(f"First like {prisca.likes}")

        if existing_like:

            # If like already exists, delete it
            existing_like.delete()
            # Decrease likes count of the event
            likes -= 1
            prisca.likes = likes

            print(f"Inside existing {prisca.likes}")
            prisca.save()
        else:
            # If like doesn't exist, create a new one
            ok = EventLikeSerializer(data=request.data)
            if ok.is_valid():
                # Increase likes count of the event
                likes += 1
                prisca.likes = likes

                print(f"Inside new {prisca.likes}")
                prisca.save()
                print(f"Saved! {prisca.likes}")
                ok.save()
                return Response(ok.data, status=HTTP_201_CREATED)

        # Return existing_like if it was deleted
        return Response(EventLikeSerializer(existing_like).data, status=HTTP_200_OK)


class LikedEventsViewApi(ListAPIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        user_id = self.kwargs["user_id"]  # Get userid from URL params
        return Event.objects.filter(event_likes__user=user_id).order_by("-likes")
