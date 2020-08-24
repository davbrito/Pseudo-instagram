from django.contrib.auth import get_user_model
from notifications.models import Notification
from rest_framework import serializers

from profiles.models import Profile
from timeline.models import Comment, Post
from timeline.serializers import CommentHyperlink

MODEL_VIEW_NAME_MAPPING = {
    Post: 'post-detail',
    Comment: 'post-comment-detail',
    Profile: 'user-profile',
    get_user_model(): 'user-detail',
}


class HyperlinkedGenericRelatedField(serializers.RelatedField):
    def __init__(self, **kwargs):
        kwargs['read_only'] = True
        super().__init__(**kwargs)

    def to_representation(self, value):
        kwargs = {'view_name': MODEL_VIEW_NAME_MAPPING[type(value)]}
        if isinstance(value, get_user_model()):
            kwargs['lookup_field'] = 'username'

        if isinstance(value, Comment):
            field = CommentHyperlink(**kwargs)
        else:
            field = serializers.HyperlinkedIdentityField(**kwargs)

        field.parent = self
        return field.to_representation(value)


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    actor = HyperlinkedGenericRelatedField()
    action_object = HyperlinkedGenericRelatedField()
    target = HyperlinkedGenericRelatedField()

    class Meta:
        model = Notification
        fields = ("url", "id", "actor", "verb", "action_object", "target",
                  "data", "deleted", "description", "emailed", "level",
                  "public", "recipient", "timestamp", "unread")

        extra_kwargs = {'recipient': {'lookup_field': 'username'}}
