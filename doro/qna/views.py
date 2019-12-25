from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Questions

# Create your views here.


class AdopterOwnQuestions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Questions.objects.filter(question_type="adopter", type__type="own")
        data_dict = {}
        count = 0
        for question in questions:
            count +=1
            if question.answer_details is not None:
                options = [x for x in question.answer_details.split(',')]
            else:
                options = []
            data_dict[count] = {'question':question.question, 'type':question.answer_type,
                                'options':options}
        return Response(data_dict)


class AdopterFoundQuestions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Questions.objects.filter(question_type="adopter", type__type="found")
        data_dict = {}
        count = 0
        for question in questions:
            count +=1
            if question.answer_details is not None:
                options = [x for x in question.answer_details.split(',')]
            else:
                options = []
            data_dict[count] = {'question':question.question, 'type':question.answer_type,
                                'options':options}
        return Response(data_dict)