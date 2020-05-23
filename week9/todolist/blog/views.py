from django.shortcuts import render, redirect
from .models import Post
import datetime

# Create your views here.
def index (request):
    return render (request, 'index.html')

def main (request):
    posts = Post.objects.all()
    return render (request, 'main.html', {'posts' : posts})

def detail(request, pk_selected):
    print(pk_selected)
    post = Post.objects.get(pk=pk_selected)
    return render(request, 'detail.html', {'post' : post})

def new (request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            pubdate = request.POST['pubdate']
        )
        return redirect ('detail', new_post.pk)
    return render (request, 'new.html')


def edit (request, pk_selected):
    post = Post.objects.get(pk=pk_selected)
    if request.method == 'POST':
        Post.objects.filter(pk=pk_selected).update(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect ('detail', pk_selected)
    return render (request, 'edit.html', {'post':post})

def delete (request, pk_selected):
    post = Post.objects.get(pk=pk_selected)
    post.delete()
    return redirect ('main')


#

# def new(request):
#     if request.method == "POST":
#         new_post = Post.objects.create(
#             title = request.POST['title'],
#             content = request.POST['content']
#         )
#         return redirect ('detail', new_post.pk)
#     return render(request, 'new.html')


# def detail(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
#     return render(request, 'detail.html', {'post' : post})

# def delete (request, post_pk):
#     post = Post.objects.get(pk=post_pk) #특정 pk의 포스트를 갖고 와서
#     post.delete() #삭제해준다.
#     return redirect('home')

# def edit (request, post_pk):
#     post = Post.objects.get(pk=post_pk)
#     if request.method == "POST":
#         Post.objects.filter(pk=post_pk).update(
#             title = request.POST['title'],
#             content = request.POST['content']
#         )
#         return redirect('detail', post_pk)
#     return render (request, 'edit.html', {'post' :post})