from django.urls import include, path

from .views import OrganizationPing

urlpatterns = [
    path("ping", OrganizationPing.as_view()),
]
