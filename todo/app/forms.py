from django import forms
from .models import Todopage


class Todoform(forms.ModelForm):
    class Meta:
        model = Todopage
        fields = ['tasks']
