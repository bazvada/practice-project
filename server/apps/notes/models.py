from django.db import models

# Create your models here.
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
