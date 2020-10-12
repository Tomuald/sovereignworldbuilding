from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group

# Remember to un-comment after creating a superuser
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, created, **kwargs):
    if created:
        user_group = Group.objects.get(name='BaseUserGroup')
        instance.groups.add(user_group)
