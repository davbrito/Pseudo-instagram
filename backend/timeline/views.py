from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.response import Response

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class CommentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows comments to be viewed or edited.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = GroupSerializer
# #     permission_classes = [permissions.IsAuthenticated]
class CommentList(generics.ListCreateAPIView):
    """
    List all comments, or create a new comment.
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Post.objects.get(id=self.kwargs['post_id']).comment_set.all()

    def get_serializer_context(self):
        return {
            'post': Post.objects.get(id=self.kwargs['post_id']),
            **super().get_serializer_context(),
        }


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List all comments, or create a new comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-posted')
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
