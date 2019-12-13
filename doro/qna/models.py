from django.db import models
from poster.models import Type, UserProfile


# Create your models here.
class Questions(models.Model):
    type = models.ForeignKey(Type, null=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Questions, null=False, blank=False, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer