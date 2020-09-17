from django.conf import settings
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from notifications.signals import notify

from .models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(m2m_changed, sender=Profile.following.through)
def notify_follow(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            profile = model.objects.get(pk=pk)
            notify.send(
                recipient=profile.user,
                sender=instance.user,
                verb='followed you',
                description=f'{instance.username()} has followed you',
            )
