from django.urls import path
from .views import (
    HomeTaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskCreateView,
    UserDetailView, UserUpdateView,
    AssignedUserCreateView,
)

urlpatterns = [
    path('new/', TaskCreateView.as_view(), name='task_create'),
    path('task-<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task-<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task-<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('assegnee/create/', AssignedUserCreateView.as_view(), name='assignee_create'),

    path('user-<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user-<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),


    path('', HomeTaskListView.as_view(), name='home'),
]