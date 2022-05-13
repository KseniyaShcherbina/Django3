
from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('clock')

    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks })

def about(request):
    return render(request, 'main/about.html')

def create(request):
    form = TaskForm
    context = {
        'form': form
    }
    return render(request, 'main/create.html',context)