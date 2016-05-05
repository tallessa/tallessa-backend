from rest_framework import permissions


class TeamPermission(permissions.BasePermission):
    message = 'Team does not match'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and getattr(obj, 'is_public', False):
            return True

        return obj.team == request.team


class TeamUserPermission(permissions.BasePermission):
    message = 'Team user permission required'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and getattr(obj, 'is_public', False):
            return True

        return request.user.groups.filter(pk__in=[obj.team.admin_group, obj.team.user_group]).exists()
