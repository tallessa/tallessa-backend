from rest_framework import permissions


class TenantPermission(permissions.BasePermission):
    message = 'Tenant does not match'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and getattr(obj, 'is_public', False):
            return True

        return obj.tenant == request.tenant


class TenantUserPermission(permissions.BasePermission):
    message = 'Tenant user permission required'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and getattr(obj, 'is_public', False):
            return True

        return request.user.groups.filter(pk__in=[obj.tenant.admin_group, obj.tenant.user_group]).exists()
