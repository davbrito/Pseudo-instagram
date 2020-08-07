from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Post

# class UserSerializer(serializers.)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['user', 'created', 'post', 'text']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    comments = CommentSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Post
        fields = ['url', 'user', 'posted', 'image', 'description', 'comments']
