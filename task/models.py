from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Task(models.Model):
    STATUS_OPT = (
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
        ('deleted', 'Deleted')
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_OPT, default='to-do')
    assignee= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

