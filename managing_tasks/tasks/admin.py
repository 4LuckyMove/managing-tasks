from django.contrib import admin
from .models import Task, AssignUserTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'creation_date', )
    list_display_links = ('title', )
    list_filter = ('creation_date', 'status', )


@admin.register(AssignUserTask)
class AssignUserTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', )
    list_display_links = ('user',)
    list_filter = ('user',)
