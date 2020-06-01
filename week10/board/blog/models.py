from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Article (models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length = 100)
    time = models.DateTimeField(auto_now=True)
    due = models.CharField(max_length=8, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')

    def __str__(self):
        return self.title

class Comment (models.Model):
    linktag = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')