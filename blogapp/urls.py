from django.contrib import admin
from django.urls import path
from . import views
from .views import (PostListView , PostDetailView , PostCreateView , UserPostListView, PostUpdateView , PostDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(), name='user_post'),
    path('', PostListView.as_view() , name='blog-home'),
    path('post/new_blog/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
