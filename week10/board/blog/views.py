from django.shortcuts import render
from .models import Article

# Create your views here.
def index (request):
    article = Article.objects.all()
    context = {'article' : article}
    return render(request, 'index.html', context)