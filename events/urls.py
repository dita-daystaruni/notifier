from django.urls import path
from .views import ListAllEvents, ListDueEvents, RetrieveEventByID, RetrieveEventByName

urlpatterns = [
    path("due", ListDueEvents.as_view()),
    path("all", ListAllEvents.as_view()),
    path("lookup/<uuid:id>", RetrieveEventByID.as_view()),
    path("search/<str:name>", RetrieveEventByName.as_view()),
]
