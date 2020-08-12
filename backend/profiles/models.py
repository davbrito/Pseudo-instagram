import os.path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import images
from django.db import models


def profile_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f'uploads/user_{instance.user.id}/profile{extension}'


def default_profile_picture():
    return images.ImageFile(
        os.path.join(settings.MEDIA_ROOT, 'default_profile.jpg'))


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='profile')
    picture = models.ImageField('profile picture',
                                upload_to=profile_directory_path,
                                blank=True)
    bio = models.TextField('profile bio', blank=True)
    followed = models.ManyToManyField('Profile',
                                      related_name='followers',
                                      blank=True)