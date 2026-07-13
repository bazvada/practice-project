from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .permissions import ReadOnlyOrAdmin

from .models import Post
from .serializers import PostSerializer

class PostListView(ListView):
    model = Post
    ordering = 'id'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ReadOnlyOrAdmin,)
