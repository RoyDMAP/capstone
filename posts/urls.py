from django.urls import path
from .views import ListPostsView , CreatePostView, SaveCommentView, ListBookmarkView


urlpatterns = [

     path("list/", ListPostsView.as_view(), name="list_posts"),
     path('create/', CreatePostView.as_view(), name="create_post"),
     path('save_comment/', SaveCommentView.as_view(), name="save_comment"),
     path('bookmarks/', ListBookmarkView.as_view(), name="bookmarks"),
   
]