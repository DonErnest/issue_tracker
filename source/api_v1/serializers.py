from django.contrib.auth.models import User

from accounts.models import GitHubRepo
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


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password','password_confirm', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'],
                    first_name = self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        user.set_password(password)
        user.save()
        GitHubRepo.objects.create(user=user)
        return user