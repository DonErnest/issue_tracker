from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, SAFE_METHODS

from api_v1.permissions import IsTeamMemberOrReadOnly
from webapp.models import Task, Project
from api_v1.serializers import TaskSerializer, ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeamMemberOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer