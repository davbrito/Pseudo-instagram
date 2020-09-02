from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Comment, Post


class CommentHyperlink(serializers.HyperlinkedIdentityField):
    view_name = 'post-comment-detail'

    def __init__(self, **kwargs):
        super().__init__(view_name=self.view_name, **kwargs)

    def get_url(self, obj, view_name, request, format):
        # Unsaved objects will not yet have a valid URL.
        if hasattr(obj, 'pk') and obj.pk in (None, ''):
            return None
        url_kwargs = {'parent_lookup_post__pk': obj.post.pk, 'pk': obj.pk}
        return reverse(view_name,
                       kwargs=url_kwargs,
                       request=request,
                       format=format)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = CommentHyperlink()

    def save(self, **kwargs):
        return super().save(user=self.context['request'].user,
                            post=self.context['post'],
                            **kwargs)

    class Meta:
        model = Comment
        fields = [
            'url',
            'user',
            'created',
            'post',
            'text',
        ]
        read_only_fields = ('user', 'created', 'post')
        extra_kwargs = {'user': {'lookup_field': 'username'}}


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    likes_count = serializers.IntegerField(read_only=True,
                                           source='likes.count')
    likes_list = serializers.HyperlinkedIdentityField(view_name='post-likes')

    love = serializers.SerializerMethodField()

    def save(self, **kwargs):
        return super().save(user=self.context['request'].user, **kwargs)

    def get_love(self, obj: Post):
        request = self.context['request']
        if request.user and request.user.is_authenticated:
            return request.user.profile.loves(obj)
        return None

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'posted',
            'image',
            'description',
            'likes_count',
            'likes_list',
            'comments',
            'love',
        ]
        read_only_fields = ['user']
        extra_kwargs = {'user': {'lookup_field': 'username'}}
