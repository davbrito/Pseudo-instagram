import notifications.settings
from django.shortcuts import redirect
from rest_framework import permissions, response, status, viewsets
from rest_framework.decorators import action

from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated, )
    only_unread = False

    def get_queryset(self):
        if notifications.settings.get_config()['SOFT_DELETE']:
            qset = self.request.user.notifications.active()
        if self.only_unread:
            qset = self.request.user.notifications.unread()
        else:
            qset = self.request.user.notifications.all()
        return qset

    @action(methods=['get'], detail=False, only_unread=True)
    def unread(self, request, **kwargs):
        return self.list(request)

    @action(methods=['post'], detail=False)
    def mark_all_as_read(self, request, **kwargs):
        self.get_queryset().mark_all_as_read()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def mark_as_read(self, request, **kwargs):
        self.get_object().mark_as_read()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
