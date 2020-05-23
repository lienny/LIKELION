from django.shortcuts import render, redirect
from .models import Article, Announcement, Question
import datetime

# Create your views here.
def index (request):
    return render(request, 'index.html')
    
def general(request):
    articles = Article.objects.all()
    articles_number = articles.count()
    return render(request, 'general.html', {
        'general': articles,
        'articles_number' : articles_number
        })

def notice(request):
    announcements = Announcement.objects.all()
    announcements_number = announcements.count()
    return render(request, 'notice.html', {
        'notice': announcements,
        'announcements_number' : announcements_number
        })

def qa(request):
    questions = Question.objects.all()
    questions_number = questions.count()
    return render(request, 'qa.html', {
        'qa': questions,
        'questions_number' : questions_number
        })

def detail_general(request, pk_selected):
    article = Article.objects.get(pk=pk_selected)
    return render(request, 'detail_general.html', {'detail_general': article})

def detail_notice(request, pk_selected):
    announcement = Announcement.objects.get(pk=pk_selected)
    return render(request, 'detail_notice.html', {'detail_notice': announcement})

def detail_qa(request, pk_selected):
    question = Question.objects.get(pk=pk_selected)
    return render(request, 'detail_qa.html', {'detail_qa': question})

def write_general(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            time = datetime.datetime.now()
        )
        return redirect('detail_general', pk_selected = new_article.pk)
    return render(request, 'write_general.html')

def write_notice(request):
    if request.method == 'POST':
        new_announcement = Announcement.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail_notice', pk_selected = new_announcement.pk)
    return render(request, 'write_notice.html')

def write_qa(request):
    if request.method == 'POST':
        new_question = Question.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail_qa', pk_selected = new_question.pk)
    return render(request, 'write_qa.html')




