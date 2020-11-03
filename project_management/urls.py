from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='project_home'),
    path('add_project/', add_project, name='add_project'),
    path('add_user/', add_user, name='add_user'),
    path('update_task/<str:pk>/', UpdateTask, name='update_task'),
    path('delete_task/<str:pk>/', DeleteTask, name='delete_task')       
]