from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from notifications.signals import notify

from .models import Comment, Post


@receiver(post_save, sender=Comment)
def notify_comment(sender, instance, created, **kwargs):
    if created:
        notify.send(
            sender=instance.user,
            recipient=instance.post.user,
            verb='commented',
            action_onject=instance,
            target=instance.post,
            description='{instance.user.username} has commented your post',
        )


@receiver(m2m_changed, sender=Post.likes.through)
def notify_like(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            sender = model.objects.get(pk=pk).user
            notify.send(
                recipient=instance.user,
                sender=sender,
                verb='liked',
                target=instance,
                description=f'{sender.username} liked your post',
            )
