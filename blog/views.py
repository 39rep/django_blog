# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'