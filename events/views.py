from django.db import OperationalError
from django.utils import timezone
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)

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


class LikedEventsViewApi(ListAPIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        user_id = self.kwargs["user_id"]  # Get userid from URL params
        return Event.objects.filter(event_likes__user=user_id).order_by("-likes")


class LikedEventView(RetrieveAPIView):

    serializer_class = EventLikeSerializer
    queryset = EventLike.objects.all()
    lookup_url_kwarg = "event"

    def get_object(self):
        event = self.kwargs.get(self.lookup_url_kwarg)
        user = self.kwargs.get("user")
        return EventLike.objects.get(event=event, user=user)
