from django.contrib import admin
from .models import Post, Reactions, Comment, Bookmark

# Register your models here.
admin.site.register(Post)
admin.site.register(Reactions)
admin.site.register(Comment)
admin.site.register(Bookmark)
