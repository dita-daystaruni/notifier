from rest_framework.generics import GenericAPIView
from rest_framework.views import Response


# Create your views here.
class OrganizationPing(GenericAPIView):
    def get(request, *args, **kwargs):
        """Responds with ping"""
        return Response({"message": "pong"})
