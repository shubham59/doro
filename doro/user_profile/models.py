from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfile(User):
    user_name = models.CharField(null=True, blank=True, max_length=100)
    mobile = models.CharField(null=True, blank=True, max_length=12)
    validated = models.BooleanField(default=False)
    code = models.CharField(max_length=10, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    i_live = models.CharField(max_length=200, null=True, blank=True)
    i_am = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user_name


@receiver(post_save, sender=UserProfile)
def id_signal(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
