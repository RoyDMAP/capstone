from django.urls import path
from .views import ListPostsView 


urlpatterns = [

     path("list/", ListPostsView.as_view(), name="list_posts"),
   
]