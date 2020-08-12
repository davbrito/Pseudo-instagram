from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Comment, Post


class CommentHyperlink(serializers.HyperlinkedIdentityField):
    view_name = 'post-comment-detail'
    lookup_field = 'pk'
    lookup_url_kwarg = 'comment_pk'

    # queryset = Comment.objects.all()
    def __init__(self, **kwargs):
        super().__init__(view_name=self.view_name, **kwargs)

    def get_url(self, obj, view_name, request, format):
        # Unsaved objects will not yet have a valid URL.
        if hasattr(obj, 'pk') and obj.pk in (None, ''):
            return None
        url_kwargs = {'post_pk': obj.post.pk, 'comment_pk': obj.pk}
        url = reverse(view_name,
                      kwargs=url_kwargs,
                      request=request,
                      format=format)
        print(f'*{url=}')
        return url


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = CommentHyperlink()

    # user = UserHyperlink()

    class Meta:
        model = Comment
        fields = ['url', 'user', 'created', 'post', 'text']
        read_only_fields = ['user', 'post']
        extra_kwargs = {
            'post': {
                'lookup_field': 'pk',
                'lookup_url_kwarg': 'post_pk'
            },
            'user': {
                'lookup_field': 'username',
            },
        }


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    # comments = CommentHyperlink(many=True)

    # user = UserHyperlink()

    class Meta:
        model = Post
        fields = ['url', 'user', 'posted', 'image', 'description', 'comments']
        read_only_fields = ['user', 'comments']
        extra_kwargs = {
            'url': {
                'lookup_field': 'pk',
                'lookup_url_kwarg': 'post_pk'
            },
            'user': {
                'lookup_field': 'username',
            }
        }
