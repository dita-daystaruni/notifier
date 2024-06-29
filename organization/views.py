from rest_framework.generics import ListAPIView

from organization.models import Organization
from organization.serializers import OrganizationSerializer


class RetrieveAllOrganizations(ListAPIView):
    """Returns a list of all registerd organizations"""

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class RetriveOrganizationDueStories(ListAPIView):
    queryset = Organization.objects.prefetch_related("story_set").all()
    serializer_class = OrganizationSerializer
