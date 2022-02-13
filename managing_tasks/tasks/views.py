from django.views.generic import ListView

from .models import Task


class HomeTaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'tasks/index.html'

