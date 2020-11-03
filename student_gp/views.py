from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404, JsonResponse
from .decorators import allowed_users
from .models import MessageModel, News
from rest_framework.response import Response


@allowed_users(allowed_roles=['CP'])
def room_1(request, room_name):

    msgs = MessageModel.objects.all()[:50]
        
    room_id = request.user.groups.values_list('id', flat=True).first()
    name_room = request.user.groups.values_list('name', flat=True).first()

    news_title = News.objects.filter(room_field=str(name_room)).order_by('-published')[:1]

    if request.method == 'POST':
        room_name = request.user.groups.values_list('name', flat=True).first()
        user_group = Group.objects.get(name=str(room_name))
        remove_user = user_group.user_set.remove(request.user)
        return redirect('/')

    context = {
        'room_name': room_name, 
        'msgs':msgs, 
        'room':room_id, 
        'titles':news_title,
    }
    return render(request, 'student_gp/room_CP.html', context)

@allowed_users(allowed_roles=['DS'])
def room_2(request, room_name):
    msgs = MessageModel.objects.all()[:50]
    room_id = request.user.groups.values_list('id', flat=True).first()
    name_room = request.user.groups.values_list('name', flat=True).first()

    news_title = News.objects.filter(room_field=str(name_room)).order_by('-published')[:1]

    if request.method == 'POST':
        room_name = request.user.groups.values_list('name', flat=True).first()
        user_group = Group.objects.get(name=str(room_name))
        remove_user = user_group.user_set.remove(request.user)
        return redirect('/')

    context = {
        'room_name': room_name,
        'msgs':msgs, 
        'room':room_id,
        'titles':news_title,
    }

    return render(request, 'student_gp/room_DS.html', context)

@allowed_users(allowed_roles=['WD'])
def room_3(request, room_name):
    msgs = MessageModel.objects.all()[:50]
    room_id = request.user.groups.values_list('id', flat=True).first()
    name_room = request.user.groups.values_list('name', flat=True).first()

    news_title = News.objects.filter(room_field=str(name_room)).order_by('-published')[:1]

    if request.method == 'POST':
        room_name = request.user.groups.values_list('name', flat=True).first()
        user_group = Group.objects.get(name=str(room_name))
        remove_user = user_group.user_set.remove(request.user)
        return redirect('/')

    context = {
        'room_name': room_name, 
        'msgs':msgs, 
        'room':room_id,
        'titles':news_title,
    }

    return render(request, 'student_gp/room_WD.html', context)

@login_required(login_url='/login/')
def room(request, room_name, **kwargs):

    if request.user.groups.exists():
        user = request.user
        group_name = str(user.groups.get(user=user))
        room_name = request.user.groups.values_list('id', flat=True).first()

        if group_name == 'CP':
            return room_1(request, room_name)
        elif group_name == 'DS':
            return room_2(request, room_name)
        elif group_name == 'WD':
            return room_3(request, room_name)
        else:
            return HttpResponse('You are not authorized.')
    else:
        return redirect('/st_gp/')


def detail_view(request, slug):
    post = get_object_or_404(News, slug=slug)
    
    context = {
        'post':post,
    }

    return render(request, 'student_gp/news_detail.html', context)

def news_post(request, slug):
    posts = News.objects.all()[:10]
    context = {
        'posts':posts,
    }
    return render(request, 'student_gp/posts.html', context)