from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .models import Comment, Post
from .permissions import IsTheUserWhoCreatedItOrReadOnly
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.order_by('-created')
    serializer_class = CommentSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsTheUserWhoCreatedItOrReadOnly
    ]

    def perform_create(self, serializer):
        data = {'user': self.request.user}
        if 'post_id' in self.kwargs:
            data['post'] = Post.objects.get(id=self.kwargs['post_id'])
        serializer.save(**data)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        if 'post_id' in self.kwargs:
            return queryset.filter(post__id=self.kwargs['post_id'])
        return queryset


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-posted')
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsTheUserWhoCreatedItOrReadOnly
    ]

    def perform_create(self, serializer):
        data = {'user': self.request.user}
        serializer.save(**data)
