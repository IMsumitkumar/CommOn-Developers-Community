from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def WorkToNote(request):
    return render(request, 'notes/main_notes.html', {})
