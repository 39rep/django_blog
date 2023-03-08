# from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'