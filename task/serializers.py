from rest_framework import serializers
from task.models import Task

class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'