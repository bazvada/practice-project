from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Post

class PostListView(ListView):
    model = Post
    ordering = 'id'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text', 'image']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'image']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('note_list')
