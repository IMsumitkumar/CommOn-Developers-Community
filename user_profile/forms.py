from django.contrib.auth.models import User
from .models import Profile, SelectGroups
from django import forms


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_pic':forms.FileInput()
        }


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = SelectGroups
        fields = '__all__'
        exclude = ['user']

