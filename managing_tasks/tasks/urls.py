from django.urls import path
from .views import (
    HomeTaskListView,
)

urlpatterns = [
    path('', HomeTaskListView.as_view(), name='home'),
]