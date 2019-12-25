from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserRegistrationSerializer, UserDetailSerializer, UserProfileUpdate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated




# Create your views here.
@api_view(['POST'])
def user_register(request):
    """
    Create a New User
    """
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.create()
            if not code:
                return Response({'error': 'Some error occurred'})
            else:
                return Response({'code':code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify(request):
    """
    Verify a new user
    """
    if request.method == 'POST':
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                get_user = UserProfile.objects.get(email=serializer.data['email'], code=serializer.data['code'])
                get_user.validated = True
                get_user.save()
                token = Token.objects.get(user=get_user)
                return Response({'username':get_user.username, 'email':get_user.email, 'token':token.key,
                                 'mobile':get_user.mobile, 'name':get_user.name})
            except Exception as e:
                return Response({'error': 'The user doesn\'t exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserProfile(APIView):
    """
    Update User Profile
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = UserProfile.objects.get(email=request.user.email)
        return Response({'name':user.name, 'mobile':user.mobile, 'email':user.email, 'i_am':user.i_am,
                         'i_live':user.i_live, 'address':user.address})

    def post(self, request, format=None):
        serializer = UserProfileUpdate(data=request.data)
        if serializer.is_valid():
            get_user = UserProfile.objects.get(email=request.user.email)
            get_user.name = serializer.data['name']
            get_user.mobile = serializer.data['mobile']
            get_user.i_live = serializer.data['i_live']
            get_user.i_am = serializer.data['i_am']
            get_user.address = serializer.data['address']
            get_user.save()
            return Response({'status':'Successfully Saved'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


