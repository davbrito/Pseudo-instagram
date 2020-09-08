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
                                                source='user.posts')
    following = serializers.HyperlinkedIdentityField(
        view_name='user-profile-following',
        lookup_field='user',
        lookup_url_kwarg='username')
    followers = serializers.HyperlinkedIdentityField(
        view_name='user-profile-followers',
        lookup_field='user',
        lookup_url_kwarg='username')

    class Meta:
        model = Profile
        fields = [
            'user',
            'picture',
            'bio',
            'following',
            'followers',
            'posts',
        ]
        read_only_fields = ('user', 'following')
        extra_kwargs = {'user': {'lookup_field': 'username'}}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'email',
            'profile',
        ]

        extra_kwargs = {'url': {'lookup_field': 'username'}}

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = super().create(validated_data)
        ProfileSerializer().update(instance=user.profile,
                                   validated_data=profile)
        return user
