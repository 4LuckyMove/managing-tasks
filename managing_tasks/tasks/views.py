from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Task
from .forms import TaskForm, UserForm


class HomeTaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'tasks/task_list.html'
    login_url = 'login'
    ordering = ['-creation_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeTaskListView, self).get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(owner=self.request.user)
        return context

    def get_queryset(self):
        if self.request.GET.get('q') == None:
            status_filter = Task.objects.all()
        elif self.request.GET.get('q') != None:
            q = self.request.GET.get('q')
            status_filter = Task.objects.filter(status__iexact=q)
        else:
            q = ''
            status_filter = Task.objects.filter(status__iexact=q)
        return status_filter


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = 'tasks/task_detail.html'
    login_url = 'login'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    context_object_name = 'task_update'
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task_delete'
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task_create'
    template_name = 'tasks/task_create.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user_detail'
    template_name = 'tasks/user_detail.html'
    login_url = 'login'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserForm
    slug_field = 'user_name'
    slug_url_kwarg = 'user_name'
    context_object_name = 'user_update'
    template_name = 'tasks/user_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.email == self.request.user
