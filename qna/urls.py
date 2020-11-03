from .import views
from django.urls import path

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('task-list/',views.taskList, name="task-list"),

    path('ques-save/<str:pk>/',views.SaveQuesItem, name="ques-save"),
    path('ans-save/<str:pk>/',views.SaveAnsItem, name="ans-save"),

    path('task-create/',views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/',views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/',views.taskDelete, name="task-delete"),

    path('QnA/',views.QnA, name='qna'),
]