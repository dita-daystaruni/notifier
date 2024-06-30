from django.db import OperationalError
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView

from events.models import Event
from events.serializers import EventSerializer


# Create your views here.
class ListDueEvents(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(
        start_date__lt=timezone.now(), end_date__gt=timezone.now()
    ).order_by("-likes")


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
