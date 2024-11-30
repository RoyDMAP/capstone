from django.urls import path
from .views import ListPostsView , CreatePostView


urlpatterns = [

     path("list/", ListPostsView.as_view(), name="list_posts"),
     path('create/', CreatePostView.as_view(), name="create_post"),
   
]