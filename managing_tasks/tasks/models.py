from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    title = models.CharField('Title', max_length=150)
    description = models.TextField('Description')
    status = models.CharField(
        'Status',
        choices=[('', 'Not completed'), ('1', 'Сompleted')],
        max_length=1,
        blank=True,
    )
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), verbose_name='Owner', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': str(self.id)})

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
