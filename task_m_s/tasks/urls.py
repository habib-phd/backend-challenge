from django.urls import path
from . import views

urlpatterns = [
    
    path('tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
    path('labels/', views.LabelListCreate.as_view(), name='label-list-create'),
    path('labels/<int:pk>/', views.LabelRetrieveUpdateDestroy.as_view(), name='label-retrieve-update-destroy'),
    
]
