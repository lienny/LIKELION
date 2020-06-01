from django.shortcuts import render, redirect
from .models import Article, Comment
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    articles = Article.objects.all().order_by('due')
    context = {'articles' : articles}
    return render(request, 'index.html', context)

@login_required(login_url='/registration/login')
def new (request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due'],
            author = request.user
        )
        return redirect('detail', new_article.pk)
    return render (request, 'new.html')

def detail(request, pk_select):
    article = Article.objects.get(pk=pk_select)
    context = {'article_detail':article}

    if request.method == 'POST':
        Comment.objects.create(
            linktag = article,
            content = request.POST['content'],
            author = request.user
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

def signup (request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', { 'error' : error })

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', { 'error': error })

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')