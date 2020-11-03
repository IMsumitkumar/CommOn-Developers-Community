from .models import CreateGroup
from django import forms

class UserGroupForm(forms.ModelForm):
    class Meta:
        model = CreateGroup
        fields = '__all__'
        exclude = ['user']