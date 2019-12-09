from django.core.serializers import json
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, SAFE_METHODS, \
    DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.permissions import IsTeamMemberOrReadOnly
from webapp.models import Task, Project
from api_v1.serializers import TaskSerializer, ProjectSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, IsTeamMemberOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['project']


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class RegisterView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer  = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'response': 'Регистрация прошла успешно!',
                             'first_name': user.first_name,
                             'last_name': user.last_name})
        else:
            return Response({serializer.errors})



class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok', 'message':'Вы вышли'})