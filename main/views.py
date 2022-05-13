
from django.shortcuts import render, redirect
from .models import Task, Comment
from .forms import CommentForm

def index(request):
    tasks = Task.objects.order_by('clock')

    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks })

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'comments': comments,
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html',context)