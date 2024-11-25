from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.views.generic import ListView
from django.urls import reverse
from .forms import NoteForm
from .models import Note

# Create your views here.
"""
    ListView = get a list of records
    DetailView = get the details of a record
    CrateView = create a new record
    DeleteView = delete record
    UpdateView = update record
    LoginView = login 
"""




class CreateNoteView(CreateView):
    template_name="notes/create_note.html"
    form_class = NoteForm


    def get_success_url(self):
        return reverse('list_notes')
    
class ListNotesView(ListView):
    template_name = "notes/list_note.html"
    model = Note