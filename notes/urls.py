from django.urls import path
from .views import CreateNoteView, ListNotesView


urlpatterns = [
    path("create/", CreateNoteView.as_view(), name="create_note"),
    path("list/", ListNotesView.as_view(), name="list_notes"),
]
