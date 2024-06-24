from django.urls import path

from .views import OrganizationPing

urlpatterns = [
    path("ping", OrganizationPing.as_view()),
]
