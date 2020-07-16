rfrom django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.title
        
    def date(self):
        return self.pubdate.strftime('%b %e %Y')