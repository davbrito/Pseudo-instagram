from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        return (
            # read only always permitted
            request.method in permissions.SAFE_METHODS
            # write only allowed to the owner of the post/comment
            or obj.user == request.user)


class ItsYourselfOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, user_obj):
        """Se otorga permiso de escritura si es su propio usuario"""
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        return (
            # read only always permitted
            request.method in permissions.SAFE_METHODS
            # write only allowed to the owner of the post/comment
            or user_obj == request.user)


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.method in permissions.SAFE_METHODS
