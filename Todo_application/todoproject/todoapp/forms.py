from django import forms
from .models import todomodel


class todos(forms.ModelForm):
    class Meta:
        model = todomodel
        fields = ['name', 'priority', 'date']