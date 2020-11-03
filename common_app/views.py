from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy

# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})

@login_required()
def GpList(request):
    return render(request, 'index_gp.html')

class UserLogin(TemplateView):
    template_name = 'common_app/auth_login.html'

# Register
class UserRegister(CreateView):
    form_class = forms.UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'common_app/auth_register.html'