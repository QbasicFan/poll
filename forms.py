from django import forms
from .models import poll




class pollForm(forms.ModelForm):
    class Meta:
        model = poll
        fields = ['title','menu','footer','body']
