from django.contrib import admin
from board.models import Article
from board.models import Question
from board.models import Announcement

# Register your models here.
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Announcement)