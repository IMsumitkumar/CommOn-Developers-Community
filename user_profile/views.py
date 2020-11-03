from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, GroupCreateForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponse, Http404
# Create your views here.


@login_required(login_url='login')
def UserProfile(request):

    current_user = request.user
    profile = Profile.objects.filter(user=current_user)

    # context = {'profile':profile}
    return render(request, 'user_profile/user_profile.html', {'profile':profile})


@login_required(login_url='login')
def account_settings(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile:user_profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {'p_form':p_form}
    return render(request, 'user_profile/user_account_settings.html', context)



@login_required(login_url='login')
def group_choice(request):

    if request.method == 'POST':
        g_form = GroupCreateForm(request.POST, request.FILES)
        if g_form.is_valid():
            instance = g_form.save(commit=False)
            instance.user = request.user
            instance.save()
            user = request.user
            # print(g_form.cleaned_data.get('groups'))

            gp = str(g_form.cleaned_data.get('groups'))
            if gp == 'CP':
                group = Group.objects.get(name='CP')
                user.groups.add(group)
            elif gp == 'DS':
                group = Group.objects.get(name='DS')
                user.groups.add(group)
            elif gp == 'WD':
                group = Group.objects.get(name='WD')
                user.groups.add(group)
            else:
                return redirect('/st_gp/')

            return redirect('/st_gp/my_room/')
    else:
        g_form = GroupCreateForm()

    
    context = {'g_form':g_form}
    return render(request, 'user_profile/choices.html', context)

