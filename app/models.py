from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Author(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')], default='D',)
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="_", db_index=True, unique=True)
    post = models.ForeignKey(Post,  models.SET_NULL, null=True, blank=True, related_name='category')

    def __str__(self):
        return self.title






