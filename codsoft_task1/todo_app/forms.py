from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'category': forms.TextInput(attrs={'placeholder': 'E.g. Work, Personal'}),
        }
