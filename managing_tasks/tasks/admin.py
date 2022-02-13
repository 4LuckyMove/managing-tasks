from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'creation_date', )
    list_display_links = ('title', )
    list_filter = ('id', 'title', 'status', )