from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Task
from .forms import TaskForm


class HomeTaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'tasks/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'tasks/task_detail.html'


class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task_update'
    form_class = TaskForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'tasks/task_edit.html'


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task_delete'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('home')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task_create'
    template_name = 'tasks/task_create.html'
