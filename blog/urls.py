from django.urls import path
from . import views
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,DoubtListView,DoubtCreateView,DoubtDetailView

urlpatterns = [
    path('', views.home,name="blog-home"),
    
    path('posts/',PostListView.as_view(),name="blog-posts"),
    path('posts/post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('posts/post/new/',PostCreateView.as_view(),name='post-create'),
    path('posts/post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('posts/post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('posts/user/<str:username>',UserPostListView.as_view(),name="user-posts"),
    path('doubts/',DoubtListView.as_view(),name="blog-doubts"),
    path('doubts/doubt/<int:pk>/',DoubtDetailView.as_view(),name='doubt-detail'),
    path('doubts/doubt/newd/',DoubtCreateView.as_view(),name='doubt-create'),
    


]
