from django import forms
from .models import AskTeam

class askTeamForm(forms.ModelForm):
    class Meta:
        model = AskTeam
        fields = [
            'title',
            'description',
            'team_size',
            'tags',
        ]
