from django.shortcuts import render
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import SemesterSerializer, SemesterEvenSerializer
from .models import Semester, SemesterEvent


# Create your views here.
class CurrentSemesterView(ListAPIView):
    queryset = Semester.objects.filter(
        end_date__gt=timezone.now(),
    )
    serializer_class = SemesterSerializer


class ListAllSemestersView(ListAPIView):
    queryset = Semester.objects.all().order_by("-start_date")
    serializer_class = SemesterSerializer


class ListAllSemesterEvents(ListAPIView):
    queryset = SemesterEvent.objects.all()
    lookup_field = "semester"
    lookup_url_kwarg = "semester"
    serializer_class = SemesterEvenSerializer
