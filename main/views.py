
from django.shortcuts import render
from .models import Task, Comment
from .forms import CommentForm

def index(request):
    tasks = Task.objects.order_by('clock')

    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks })

def about(request):
    return render(request, 'main/about.html')

def create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'comments': comments,
        'form': form
    }
    return render(request, 'main/create.html',context)