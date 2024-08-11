from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('kanban/', views.kanban_board, name='kanban_board'),
    path('update_task_status/', views.update_task_status, name='update_task_status'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
