from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to="posts/", default="posts/default.png")

    def __str__(self):
        return self.title