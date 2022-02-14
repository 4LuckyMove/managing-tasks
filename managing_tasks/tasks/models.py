from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Task(models.Model):
    title = models.CharField('Title', max_length=150)
    description = models.TextField('Description', blank=True)
    status = models.CharField(
        'Status',
        choices=[('', 'Not completed'), ('1', 'Сompleted')],
        max_length=1,
        blank=True,
    )
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), verbose_name='Owner', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField('Slug', unique=True, db_index=True, max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
