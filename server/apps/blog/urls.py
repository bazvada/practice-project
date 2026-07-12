from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views
from .views import PostViewSet

router = SimpleRouter()

router.register('posts', PostViewSet)


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('', include(router.urls)),
]