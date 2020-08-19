import os.path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import images
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f'uploads/user_{instance.user.id}/profile{extension}'


User.Meta.ordering = ('username', )


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        editable='False',
        related_name='profile',
    )
    picture = models.ImageField(
        'profile picture',
        upload_to=profile_directory_path,
        blank=True,
    )
    bio = models.TextField(
        'profile bio',
        blank=True,
    )
    followed = models.ManyToManyField(
        'Profile',
        related_name='followers',
        blank=True,
    )

    def username(self):
        return self.user.username
