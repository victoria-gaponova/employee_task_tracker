from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline", "status", "employee")
    search_fields = ("name", "employee__full_name")
    list_filter = ("status", "deadline")
    ordering = ("deadline", "name")
    raw_id_fields = ("employee", "parent_task")
