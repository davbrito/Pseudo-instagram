from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


def user_uploads_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<year>/<month>/<day>/<filename>
    return f'uploads/user_{instance.user.id}/%Y/%m/%d/{filename}'


def profile_directory_path(instance, filename):
    return f'uploads/user_{instance.user.id}/profile/{filename}'


class PseudoIgUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    profile_image = models.ImageField('profile image',
                                      upload_to=profile_directory_path)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    image = models.ImageField('post image',
                              upload_to=user_uploads_directory_path)
    description = models.TextField('post description')


class Comment(models.Model):
    us
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
