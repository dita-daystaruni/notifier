from django.urls import path

from stories.views import DueStories

urlpatterns = [
    path("all", DueStories.as_view()),
]
