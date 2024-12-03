from django.contrib import admin
from .models import Post, Reactions

# Register your models here.
admin.site.register(Post)
admin.site.register(Reactions)
