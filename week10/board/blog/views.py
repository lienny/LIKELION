from django.shortcuts import render, redirect
from .models import Article, Comment
from datetime import datetime

# Create your views here.
def index (request):
    articles = Article.objects.all().order_by('due')
    context = {'articles' : articles}
    return render(request, 'index.html', context)

def new (request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due']
        )
        return redirect('detail', new_article.pk)
    return render (request, 'new.html')

def detail(request, pk_select):
    article = Article.objects.get(pk=pk_select)
    context = {'article_detail':article}

    if request.method == 'POST':
        Comment.objects.create(
            linktag = article,
            content = request.POST['content']
        )
        return redirect('detail', pk_select)
    return render(request, 'detail.html', context)

def delete(request, pk_select):
    article = Article.objects.get(pk=pk_select)
    article.delete()
    return redirect ('index')

def edit(request, pk_select):
    article = Article.objects.get(pk=pk_select)
    context = {'article' : article}
    if request.method == 'POST':
        Article.objects.filter(pk=pk_select).update(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due']
        )
        return redirect('detail', pk_select)
    return render(request, 'edit.html', context)

def delete_comment(request, pk_select, pk_select_comment):
    comment = Comment.objects.get(pk=pk_select_comment)
    comment.delete()
    return redirect('detail', pk_select)