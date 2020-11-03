from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('',views.WorkToNote, name='notes'),
    # url(r'^$', views.WorkToNote, name='notes'),
]