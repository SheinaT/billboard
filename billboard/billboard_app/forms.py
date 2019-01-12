from django import forms
from .models import Billboard

class PostForm(forms.ModelForm):
    class Meta:
        model = Billboard
        fields = '__all__'





