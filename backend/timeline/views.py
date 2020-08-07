from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-posted')
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class CommentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows comments to be viewed or edited.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
