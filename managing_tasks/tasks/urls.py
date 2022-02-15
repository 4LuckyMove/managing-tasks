from django.urls import path
from .views import (
    HomeTaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskCreateView,
    UserDetailView, UserUpdateView,
)

urlpatterns = [
    path('new/', TaskCreateView.as_view(), name='task_create'),
    path('task-<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task-<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task-<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('<slug:user_name>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<slug:user_name>/', UserDetailView.as_view(), name='user_detail'),

    path('', HomeTaskListView.as_view(), name='home'),
]