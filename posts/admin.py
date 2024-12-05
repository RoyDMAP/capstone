from django.contrib import admin
from .models import Post, Reactions, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Reactions)
admin.site.register(Comment)
