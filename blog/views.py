# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied

from blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_object(self):
        post = super().get_object()
        if post.is_published or self.request.user.is_authenticated:
            return post
        else:
            raise PermissionDenied