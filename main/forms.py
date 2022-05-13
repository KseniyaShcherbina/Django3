from .models import Comment
from django.forms import ModelForm, widgets, TextInput, Textarea

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ["author", "body"]
        widgets = {"author": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            "body": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите отзыв'})
        }

