from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
