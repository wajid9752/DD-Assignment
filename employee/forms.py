from django import forms
from manager.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
        
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

