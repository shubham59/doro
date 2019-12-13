from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.


class UserProfile(User):
    user_name = models.CharField(null=True, blank=True, max_length=100)
    mobile = models.CharField(null=False, blank=False, max_length=12)

    def __str__(self):
        return self.user_name
