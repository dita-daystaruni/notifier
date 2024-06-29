from django.urls import path

from stories.views import (
    DueStories,
    OrganizationDueStories,
)

urlpatterns = [
    path("all", DueStories.as_view()),
    path("org/<uuid:organization_id>", OrganizationDueStories.as_view()),
]
