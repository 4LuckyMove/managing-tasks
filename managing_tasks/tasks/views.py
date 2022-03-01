from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Task, AssignUserTask
from .forms import TaskForm, UserForm, AssignedUserCreationForm


class HomeTaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'tasks/task_list.html'
    login_url = 'login'
    ordering = ['-creation_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeTaskListView, self).get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(
            Q(owner=self.request.user) &
            Q(assignee_user__isnull=False)
        ).order_by('-creation_date')
        context['unassigned_task_list'] = Task.objects.filter(
            Q(owner=self.request.user) &
            Q(assignee_user__isnull=True)
        ).order_by('-creation_date')
        context['start_date'] = self.request.GET.get('startDate')
        context['end_date'] = self.request.GET.get('endDate')
        context['by_status'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get('q') else None
        start_date = datetime.strptime(self.request.GET.get('startDate'), '%d.%m.%Y').date() \
            if self.request.GET.get('startDate') else self.request.POST.get('startDate')
        end_date = datetime.strptime(self.request.GET.get('endDate'), '%d.%m.%Y').date() \
            if self.request.GET.get('endDate') else self.request.POST.get('endDate')

        if q != None and start_date == None and end_date == None:
            task_filter = Task.objects.filter(status__exact=q)
        elif q == None and start_date != None and end_date != None:
            task_filter = Task.objects.filter(
                Q(creation_date__date__range=[start_date, end_date]) |
                Q(creation_date__date__range=[end_date, start_date])
            )
        elif q != None and start_date != None and end_date != None:
            task_filter = Task.objects.filter(
                Q(status__exact=q, creation_date__date__range=[start_date, end_date]) |
                Q(status__exact=q, creation_date__date__range=[end_date, start_date])
            )
        else:
            task_filter = Task.objects.all()

        return task_filter


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
        full_name = self.request.user.first_name + ' ' + self.request.user.last_name
        if self.request.user.first_name and self.request.user.last_name:
            form.instance.owner = full_name
        else:
            form.instance.owner = self.request.user
        return super(TaskCreateView, self).form_valid(form)


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


class AssignedUserCreateView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = AssignedUserCreationForm
    template_name = 'tasks/assignee_create.html'
