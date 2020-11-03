from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.UserProfile, name='user_profile'),                       #user/
    path('update-profile/', views.account_settings, name='update_profile'),
    path('my-group/', views.group_choice, name='gp_choice'),
]
