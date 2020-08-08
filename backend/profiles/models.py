import os.path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.db import models


def profile_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f'uploads/user_{instance.user.id}/profile{extension}'


DEFAULT_PROFILE_PICTURE = ImageFile(
    os.path.join(settings.MEDIA_ROOT, 'default_profile.jpg'))


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    picture = models.ImageField('profile picture',
                                upload_to=profile_directory_path,
                                default=DEFAULT_PROFILE_PICTURE)
    bio = models.TextField('profile bio', blank=True)
    followed = models.ManyToManyField('self', blank=True)
