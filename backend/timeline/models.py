import os.path

# from django.contrib.auth.models import User
from django.db import models
from django.utils import html, timezone

USER_MODEL = 'auth.User'


def user_uploads_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<datetime><fileext>
    extension = os.path.splitext(filename)[1]
    return (f'uploads/user_{instance.user.id}/'
            f'{instance.posted.strftime(r"%Y%m%d_%H%M%S")}{extension}')


class Post(models.Model):
    objects: models.Manager
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

    def __str__(self):
        return (f'Post({self.id}) de {self.user.username} ({self.posted}):'
                f' "{self.description_brief()}"')

    def description_brief(self, max_length: int = 50):
        brief = html.escape(self.description)[:max_length]
        if len(self.description) > max_length - 3:
            brief += '...'
        return brief


class Comment(models.Model):
    objects: models.Manager
    user = models.ForeignKey(USER_MODEL,
                             related_name='comments',
                             on_delete=models.SET_NULL,
                             null=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)
    text = models.TextField('comment text')

    class Meta:
        ordering = ['created']
