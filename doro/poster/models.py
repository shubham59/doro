from django.db import models
from user_profile.models import UserProfile
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Poster(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Type(models.Model):
    content_type = models.ForeignKey(ContentType, null=False, blank=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{}-{}".format(self.type, str(self.content_type))