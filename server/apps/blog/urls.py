from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='note_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='note_detail'),
    path('create/', views.PostCreateView.as_view(), name='note_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='note_delete'),
]