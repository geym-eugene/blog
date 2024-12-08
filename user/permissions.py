from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
