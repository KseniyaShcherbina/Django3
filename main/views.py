from django.shortcuts import render
from .models import Task

def index(request):
    task = Task.objects.all()

    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': task })

def about(request):
    return render(request, 'main/about.html')
