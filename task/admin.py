from django.contrib import admin
from task.models import Task

# Register your models here.
@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'created_at', 'modified_at')
    search_fields = ('title', 'description')
    list_filter = ('assignee', 'status')
    raw_id_fields = ('assignee',)
    list_per_page = 5