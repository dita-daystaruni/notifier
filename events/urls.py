from django.urls import path
from .views import (
    LikeEventView,
    LikedEventsViewApi,
    ListAllEvents,
    ListDueEvents,
    RetrieveEventByID,
    RetrieveEventByName,
)

urlpatterns = [
    path("due", ListDueEvents.as_view()),
    path("all", ListAllEvents.as_view()),
    path("lookup/<uuid:id>", RetrieveEventByID.as_view()),
    path("search/<str:name>", RetrieveEventByName.as_view()),
    path("like", LikeEventView.as_view()),
    path("liked-by/<uuid:user_id>", LikedEventsViewApi.as_view()),
]
