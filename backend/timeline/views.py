from rest_framework import (decorators, permissions, serializers, status,
                            views, viewsets)
from rest_framework.request import Request
from rest_framework.response import Response

from _utilities.views import list_queryset
from profiles.serializers import ProfileSerializer

from .models import Comment, Post
from .permissions import IsTheUserWhoCreatedItOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsTheUserWhoCreatedItOrReadOnly
    ]

    lookup_field = 'pk'
    lookup_url_kwarg = 'post_pk'

    def create(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    @decorators.action(detail=True,
                       methods=['get', 'put', 'patch'],
                       url_path=r'comments/(?P<comment_pk>[\d]+)',
                       url_name='comment-detail',
                       lookup_field='pk',
                       lookup_url_kwarg='comment_pk',
                       queryset=Comment.objects.all(),
                       serializer_class=CommentSerializer,
                       permission_classes=[
                           permissions.IsAuthenticatedOrReadOnly,
                           IsTheUserWhoCreatedItOrReadOnly
                       ],
                       name='Instancia de Comentario')
    def comment_detail(self, request, post_pk=None, comment_pk=None):
        if request.method == 'GET':
            return self.retrieve(request)
        if request.method == 'PUT':
            return self.update(request)
        if request.method == 'PATCH':
            return self.partial_update(request)

    @decorators.action(detail=True,
                       methods=['get', 'post'],
                       url_path=r'comments',
                       url_name='comment-list',
                       serializer_class=CommentSerializer,
                       permission_classes=[permissions.IsAuthenticated],
                       name='Lista de Comentarios')
    def comment_list(self, request, post_pk=None):
        if request.method == 'GET':
            return list_queryset(self, self.get_object().comments.all())
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, post=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @decorators.action(detail=True,
                       methods=['get', 'post', 'delete'],
                       url_path=r'likes',
                       url_name='likes',
                       serializer_class=ProfileSerializer,
                       permission_classes=[permissions.IsAuthenticated],
                       name='Likes')
    def likes(self, request, post_pk=None):
        if request.method == 'GET':
            return list_queryset(self, self.get_object().likes.all())
        if request.method == 'POST':
            self.get_object().likes.add(request.user.profile)
            return Response(status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            self.get_object().likes.remove(request.user.profile)
            return Response(status=status.HTTP_204_NO_CONTENT)
