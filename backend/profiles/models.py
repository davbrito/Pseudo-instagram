import os.path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def profile_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f'uploads/user_{instance.user.id}/profile{extension}'


get_user_model().Meta.ordering = ('username',)


class Profile(models.Model):
    objects: models.Manager

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
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
    following = models.ManyToManyField(
        'Profile',
        related_name='followers',
        blank=True,
    )

    def username(self):
        return self.user.username  # pylint: disable=no-member

    def loves(self, post) -> bool:
        """Indica si le gusta un post determinado"""
        return post.likes.filter(pk=self.pk).exists()

    def follow(self, other):
        """Follow other profile."""
        return self.following.add(other)

    def unfollow(self, other):
        """Unfollow other profile."""
        return self.following.remove(other)

    def follows(self, other: 'Profile'):
        """Indica si es seguidor de otro perfil."""
        return self.following.filter(pk=other.pk).exists()
