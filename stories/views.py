from django.utils import timezone
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from organization.serializers import OrganizationSerializer
from stories.models import Story
from stories.serializers import StorySerializer


# Create your views here.
class DueStories(ListAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.filter(date_of_expiry__gt=timezone.now())


class OrganizationDueStories(ListAPIView):

    serializer_class = StorySerializer

    def get_queryset(self):
        organization_id = self.kwargs.get("organization_id")
        if organization_id:
            print("jeez")
            return Story.objects.filter(
                date_of_expiry__gt=timezone.now(), organization=organization_id
            )
