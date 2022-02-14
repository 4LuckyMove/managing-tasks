from django.urls import path
from .views import (
    HomeTaskListView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
)

urlpatterns = [
    path('new/', TaskCreateView.as_view(), name='task_create'),
    path('<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    path('<slug:slug>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('<slug:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('', HomeTaskListView.as_view(), name='home'),
]