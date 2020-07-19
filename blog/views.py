from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post,doubt
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    
    return render(request, 'blog/home.html')


def posts(request):
    context = {'posts': Post.objects.all()
    }

    return render(request, 'blog/posts.html', context)

def doubts(request):
    context = {'doubts': doubt.objects.all()
    }

    return render(request, 'blog/doubts.html', context)


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5



class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        p=self.request.user
        if(p.is_staff):
            return True
        return False   


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = selfLoginRequiredMixin,UserPassesTestMixin,CreateView.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if( self.request.user == post.author):
            return True
        return False   

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/posts/"

    def test_func(self):
        post = self.get_object()
        if( self.request.user == post.author):
            return True
        return False 

class DoubtListView(PostListView):
     model = doubt
     template_name = 'blog/doubts.html' #<app>/<model>_<viewtype>.html
     context_object_name = 'doubts'


class DoubtDetailView(DetailView):
    model = doubt


class DoubtCreateView(LoginRequiredMixin,CreateView):
    model = doubt
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    