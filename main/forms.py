from .models import Task
from django.forms import ModelForm, widgets, TextInput

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            "task": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отзыв'})
        }

form = TaskForm()
