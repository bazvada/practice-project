from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Note

class NoteListView(ListView):
    model = Note
    ordering = 'id'
    paginate_by = 10

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'text', 'is_important']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'text', 'is_important']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')
