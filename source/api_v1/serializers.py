from webapp.models import Task, Project
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'summary','description', 'status', 'type', 'created_at', 'updated_at', 'project', 'created_by', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description','created_at', 'updated_at','status', 'squad', 'tasks')