from rest_framework import (decorators, permissions, serializers, status,
                            views, viewsets)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from _utilities.views import list_queryset
from profiles.serializers import ProfileSerializer

from .models import Comment, Post
from .permissions import IsTheUserWhoCreatedItOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    # model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsTheUserWhoCreatedItOrReadOnly
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action in ('create', ):
            context['post'] = Post.objects.get(
                pk=self.kwargs['parent_lookup_post__pk'])
        return context


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsTheUserWhoCreatedItOrReadOnly
    ]

    @decorators.action(detail=True,
                       methods=['get', 'post', 'delete'],
                       serializer_class=ProfileSerializer,
                       permission_classes=[permissions.IsAuthenticated],
                       name='Likes')
    def likes(self, request: Request, pk=None):
        if request.method == 'GET':
            return list_queryset(self, self.get_object().likes.all())
        if request.method == 'POST':
            self.get_object().likes.add(request.user.profile)
            return Response({'detail': 'like agregado'},
                            status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            self.get_object().likes.remove(request.user.profile)
            return Response({'detail': 'like eliminado'},
                            status=status.HTTP_204_NO_CONTENT)
