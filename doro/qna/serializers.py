from .models import  UserProfile
from rest_framework import serializers


class PosterOwnAnswerSerailizer(serializers.Serializer):
    ques = serializers.CharField(max_length=1000)
    type = serializers.CharField(max_length=300)
    ans = serializers.CharField(max_length=1000)


# class AdopterOwnQuestionSerailizer(serializers.Serializer):
#     ques = serializers.CharField(max_length=1000)
#     type = serializers.CharField(max_length=300)

class AdopterQuestionsSerailizer(serializers.Serializer):
    ques = serializers.CharField(max_length=1000)
    type = serializers.CharField(max_length=300)
    ans = serializers.CharField(max_length=1000)
