from django.urls import path
from .views import *


urlpatterns = [
    path('', recruit_view, name="ask_team"),
    path('req-for-team/', index, name="team_home"),
    path('post/<slug:slug>/', detail_view, name="detail"),
    path('tag/<slug:slug>/', tagged, name="tagged"),


]
