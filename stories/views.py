from django.utils import timezone
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from stories.models import Story
from stories.serializers import StorySerializer


# Create your views here.
class DueStories(ListAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.filter(date_of_expiry__gt=timezone.now())
