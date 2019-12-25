from .models import  UserProfile
from rest_framework import serializers
from django.core.mail import EmailMessage
from random import randint


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self):
        code = randint(1000, 9999)
        try:
            #flag = EmailMessage('Authentication Code', code, to=[self.data['email']]).send()
            flag = 1
            if flag and not UserProfile.objects.filter(email=self.data['email']).exists():
                instance = UserProfile.objects.create(email=self.data['email'], code=code, username=self.data['email'])
                return instance.code
            else:
                instance = UserProfile.objects.get(email=self.data['email'])
                instance.code = code
                instance.save()
                return instance.code
        except Exception as e:
            print(e)
            return False


class UserDetailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)
    code = serializers.IntegerField()


class UserProfileUpdate(serializers.Serializer):
    mobile = serializers.CharField(max_length=12)
    name = serializers.CharField(max_length=200)
    i_live = serializers.CharField(max_length=200)
    i_am = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=1000)








