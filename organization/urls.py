from django.urls import path

from .views import (
    RetrieveAllOrganizations,
    RetriveOrganizationDueStories,
)

urlpatterns = [
    path("all", RetrieveAllOrganizations.as_view()),
    path("due", RetriveOrganizationDueStories.as_view()),
]
