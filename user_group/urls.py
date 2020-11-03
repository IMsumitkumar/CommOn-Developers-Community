from .import views
from django.urls import path

app_name = 'ug_api'

urlpatterns = [
    path('',views.apiOverview, name="ug_api-overview"),
    path('group-list/',views.groupList, name="group-list"),
    path('group-detail/<str:pk>/',views.groupDetail, name="group-detail"),
    path('group-create/',views.groupCreate, name="group-create"),
    path('group-update/<str:pk>/',views.groupUpdate, name="group-update"),
    path('group-delete/<str:pk>/',views.groupDelete, name="group-delete"),


    path('groups/', views.GroupList, name="grouplist"),
    path('<str:room_name>/', views.room, name='room'),
]