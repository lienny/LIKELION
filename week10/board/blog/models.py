from django.db import models
from django.utils import timezone

# Create your models here.
class Article (models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length = 100)
    time = timezone.now()

    def __str__(self):
        return self.title