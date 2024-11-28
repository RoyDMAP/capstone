from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class ListPostsView(ListView):
    template_name = "posts/list_post.html"
    model = Post
