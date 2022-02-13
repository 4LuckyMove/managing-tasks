from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=150, blank=True, null=True)
    description = models.TextField('Description', blank=True)
    status = models.CharField(
        'Status',
        choices=[('', 'Select status'), ('1', 'Сompleted'), ('2', 'Not completed')],
        max_length=1,
        blank=True,
    )
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    assignee = models.ForeignKey(get_user_model(), verbose_name='Assignee', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
