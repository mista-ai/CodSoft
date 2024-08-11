from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'category', 'id')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description')
    ordering = ('priority', 'status')
