from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile

DEFAULT_PROFILE_PICTURE = 'default_profile.jpg'


class ProfilePictureField(serializers.ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(allow_null=True, *args, **kwargs)

    def to_representation(self, value):
        if not value:
            url = settings.MEDIA_URL + DEFAULT_PROFILE_PICTURE
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(url)
            return url
        return super().to_representation(value)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # serializers.ImageField
    picture = ProfilePictureField()
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
            }
        }
