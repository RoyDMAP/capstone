from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post, Reactions
from .forms import PostForm, ReactionForm
from django.urls import reverse
from users.models import Profile
from django.shortcuts import redirect

# Create your views here.
class ListPostsView(ListView):
    template_name = "posts/list_post.html"
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        data = super().get_queryset().order_by('-created_on')
        for post in data: 
            post.author_profile = Profile.objects.filter(user=post.author).first()
            post.likes = Reactions.objects.filter(post=post).filter(react_type='like').count()
            post.hearts = Reactions.objects.filter(post=post).filter(react_type='heart').count()
        return data
    
    def post(self, request, *args, **kwags):
        #handle reactions
        form = ReactionForm(request.POST)
        if form.is_valid():
            react_type = form.cleaned_data['react_type']
            post_id = request.POST.get('post_id')
            post = Post.objects.get(id=post_id)

            # create the reaction
            Reactions.objects.update_or_create(
                user=request.user,
                post=post,
                defaults={'react_type': react_type}
            )
            return redirect('list_posts')
    
class CreatePostView(CreateView):
    template_name = "posts/create_post.html"
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse ('list_posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user # logged in user
        return super().form_valid(form)
