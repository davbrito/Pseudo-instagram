from rest_framework import permissions
from rest_framework.request import Request


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        x = (
            # read only always permitted
            request.method in permissions.SAFE_METHODS
            # write only allowed to the owner of the post/comment
            or obj.user == request.user)
        return x
