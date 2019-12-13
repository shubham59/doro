from django.db import models
from poster.models import UserProfile, Type


class Adopter(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
