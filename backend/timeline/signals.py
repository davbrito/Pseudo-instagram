from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify

from .models import Comment


@receiver(post_save, sender=Comment)
def notify_comment(sender, instance, created, **kwargs):
    if created:
        notify.send(
            instance.user,
            recipient=instance.post.user,
            verb='has commented',
            action_onject=instance,
            target=instance.post,
        )
