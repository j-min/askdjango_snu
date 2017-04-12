from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)