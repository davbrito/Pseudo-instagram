import os.path

from django.conf import settings
# from django.contrib.auth.models import User
from django.db import models
from django.utils import html

from profiles.models import Profile


def user_uploads_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<datetime><fileext>
    extension = os.path.splitext(filename)[1]
    return (f'uploads/user_{instance.user.id}/'
            f'{instance.posted.strftime(r"%Y%m%d_%H%M%S")}{extension}')


class Post(models.Model):
    objects: models.Manager

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
    )
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'post image',
        upload_to=user_uploads_directory_path,
        blank=False,
    )
    description = models.TextField('post description')
    likes = models.ManyToManyField(
        Profile,
        related_name='posts_liked',
    )

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        string = 'Post({id}) de {username} ({date}): "{description_brief}"'
        return string.format(
            id=self.id,  # pylint: disable=no-member
            username=self.user.username,  # pylint: disable=no-member
            date=self.posted.strftime('%Y-%m-%d'),  # pylint: disable=no-member
            description_brief=self.description_brief(),
        )

    def description_brief(self, max_length: int = 50):
        brief = html.escape(self.description)[:max_length]
        if len(self.description) > max_length - 3:
            brief += '...'
        return brief


class Comment(models.Model):
    objects: models.Manager
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField('comment text')

    class Meta:
        ordering = ['created']
