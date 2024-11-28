from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"
