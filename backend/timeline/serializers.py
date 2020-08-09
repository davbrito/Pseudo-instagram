from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Post

# class UserSerializer(serializers.)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'posts']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['url', 'user', 'created', 'post', 'text']
        read_only_fields = ['user', 'post']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    # comments = CommentSerializer(many=True, read_only=True, default=[])
    # user = serializers.ReadOnlyField(source='user.username')

    # extra_kwargs = {'user': {'read_only': True}}

    class Meta:
        model = Post
        fields = ['url', 'user', 'posted', 'image', 'description', 'comments']
