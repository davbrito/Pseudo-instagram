from rest_framework import permissions
from rest_framework.request import Request


class IsTheUserWhoCreatedItOrReadOnly(permissions.BasePermission):
    """
    Tiene permiso solo si lo hace el usuario creador.

    Utilizado para los modelos `Post` y `Comment` donde el campo `user`
    representa el usuario que creó dicho objeto
    """

    def has_object_permission(self, request: Request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        return (
            # read only always permitted
            request.method in permissions.SAFE_METHODS
            # write only allowed to the owner of the post/comment
            or obj.user == request.user)
