from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # serializers.ImageField
    posts = serializers.HyperlinkedRelatedField(many=True,
                                                read_only=True,
                                                view_name='post-detail',
                                                source='user.posts',
                                                lookup_url_kwarg='post_pk')
    followed = serializers.HyperlinkedIdentityField(
        view_name='user-profile-followed',
        lookup_field='user',
        lookup_url_kwarg='username')
    followers = serializers.HyperlinkedIdentityField(
        view_name='user-profile-followers',
        lookup_field='user',
        lookup_url_kwarg='username')

    class Meta:
        model = Profile
        fields = ['picture', 'bio', 'followed', 'followers', 'posts']
        read_only_fields = ('followed', )
        extra_kwargs = {'post': {'source': 'user.posts'}}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'profile']

        read_only_fields = ('posts', )
        extra_kwargs = {
            'url': {
                'view_name': 'user-detail',
                'lookup_field': 'username'
            },
            'posts': {
                'lookup_url_kwarg': 'post_pk'
            }
        }
