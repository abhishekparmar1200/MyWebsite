from django.urls import path
from . import views
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', views.home,name="blog-home"),
    path('posts/',PostListView.as_view(),name="blog-posts"),
    path('posts/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('posts/post/new/',PostCreateView.as_view(),name='post-create'),
    path('posts/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('posts/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('posts/user/<str:username>',UserPostListView.as_view(),name="user-posts"),



]
