from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse
from users.models import Profile

# Create your views here.
class ListPostsView(ListView):
    template_name = "posts/list_post.html"
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        data = super().get_queryset().order_by('-created_on')
        for post in data: 
            post.author_profile = Profile.objects.filter(user=post.author).first()
        return data
    
class CreatePostView(CreateView):
    template_name = "posts/create_post.html"
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse ('list_posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user # logged in user
        return super().form_valid(form)
