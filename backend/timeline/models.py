import os.path

from django.contrib.auth.models import User
from django.db import models
from django.utils import html, timezone

USER_MODEL = User


def user_uploads_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<year>/<month>/<day>/<filename>
    extension = os.path.splitext(filename)[1]
    return (f'uploads/user_{instance.user.id}/'
            f'{instance.posted.strftime(r"%Y%m%d_%H%M%S")}{extension}')


class Post(models.Model):
    user = models.ForeignKey(USER_MODEL,
                             related_name='posts',
                             on_delete=models.SET_NULL,
                             null=True)
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('post image',
                              upload_to=user_uploads_directory_path)
    description = models.TextField('post description')

    class Meta:
        ordering = ['posted']

    def description_brief(self):
        brief = html.escape(self.description)[:50]
        if len(brief) < 47:
            brief += '...'
        return brief

    def comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    user = models.ForeignKey(USER_MODEL,
                             related_name='comments',
                             on_delete=models.SET_NULL,
                             null=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField('comment text')

    class Meta:
        ordering = ['created']
