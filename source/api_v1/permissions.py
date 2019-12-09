from rest_framework import permissions

class IsTeamMemberOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        print('entered')
        if 'pk' in view.kwargs and view.kwargs['pk']:
            obj = view.get_object()
            if request.method in permissions.SAFE_METHODS:
                return True
            return bool(request.user.team.filter(project=obj.project))
        else:
            if request.method not in permissions.SAFE_METHODS:
                project = request.data.get('project')
                return bool(request.user.team.filter(project=project))
            return True
