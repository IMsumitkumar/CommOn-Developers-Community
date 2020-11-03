from django.urls import path
from .views import room, detail_view, news_post
from user_group.views import group_create
from user_profile.views import group_choice

app_name = 'st_gp'

urlpatterns = [
    path('',group_choice, name='gp_choice'),
    path('gcr', group_create, name='gp_create'),
    path('<str:room_name>/', room, name='room'),
    path('news/<slug:slug>/', detail_view, name='news_detail' ),
    path('posts/<slug:slug>/', news_post, name='news_post'),

]