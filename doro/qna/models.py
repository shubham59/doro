from django.db import models
from poster.models import Type, UserProfile


# Create your models here.
class Questions(models.Model):
    choices_user = (('adopter', 'adopter'), ('poster', 'poster'))
    choices_answer = (('objective', 'objective'), ('full_length', 'full_length'))
    type = models.ForeignKey(Type, null=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=500, null=False, blank=False)
    question_type = models.CharField(choices=choices_user, default=1, max_length=200)
    answer_type = models.CharField(choices=choices_answer, default=2, max_length=200)
    answer_details = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Questions, null=False, blank=False, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer