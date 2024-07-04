from django.urls import path, include
from .views import CurrentSemesterView, ListAllSemesterEvents, ListAllSemestersView

urlpatterns = [
    path(
        "current",
        CurrentSemesterView.as_view(),
    ),
    path(
        "all",
        ListAllSemestersView.as_view(),
    ),
    path(
        "events/<uuid:semester>",
        ListAllSemesterEvents.as_view(),
    ),
]
