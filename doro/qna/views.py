from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Questions, Answer
from .serializers import PosterOwnAnswerSerailizer, AdopterQuestionsSerailizer
from rest_framework import status
from user_profile.models import UserProfile, Posts
from poster.models import Type
# Create your views here.


class PosterOwnQuestions(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     questions = Questions.objects.filter(question_type="adopter", type__type="own")
    #     data_dict = {}
    #     count = 0
    #     for question in questions:
    #         count +=1
    #         if question.answer_details is not None:
    #             options = [x for x in question.answer_details.split(',')]
    #         else:
    #             options = []
    #         data_dict[count] = {'question':question.question, 'type':question.answer_type,
    #                             'options':options}
    #     return Response(data_dict)

    # def get(self, request):
    #     data = AdopterOwnQuestionSerailizer(data=request.data, many=True)
    #     if data.is_valid():
    #         for i in data.data:
    #             answers = Answer.objects.filter(question__question_type="adopter", type__type="own",
    #                                       user=UserProfile.objects.get(email=request.user.email))
    #     data_dict = {}
    #     count = 0
    #     for answers in questions:
    #         count +=1
    #         if question.answer_details is not None:
    #             options = [x for x in question.answer_details.split(',')]
    #         else:
    #             options = []
    #         data_dict[count] = {'question':question.question, 'type':question.answer_type,
    #                             'options':options}
    #     return Response(data_dict)

    def get(self, request):
        type = Type.objects.get(content_type__model='poster', type='own')
        posts = Posts.objects.filter(user=UserProfile.objects.get(email=request.user.email))
        main_list = []
        for post in posts:
            answers = Answer.objects.filter(question__question_type="poster", question__type=type,
                                            user=UserProfile.objects.get(email=request.user.email), post_id=post.id)

            data_dict = {}
            data_dict['post_id'] = post.id
            details = []
            for answer in answers:
                details.append({'question':answer.question.question, 'type':answer.question.answer_type,
                                'answer':answer.answer})
            data_dict['details'] = details

            if len(data_dict['details']) == 0:
                del data_dict['post_id']
            else:
                main_list.append(data_dict)
        return Response(main_list)

    def post(self, request):
        data = PosterOwnAnswerSerailizer(data=request.data, many=True)
        type=Type.objects.get(content_type__model='poster', type='own')
        post = Posts.objects.create(user=UserProfile.objects.get(email=request.user.email))
        if data.is_valid():
            for x in data.data:
                get, created = Questions.objects.get_or_create(question=x['ques'], answer_type=x["type"],
                                                               type=type, question_type="poster")
                if not created:
                   get = Questions.objects.get(question=x['ques'], answer_type=x["type"], type=type)
                Answer.objects.create(user=UserProfile.objects.get(email=request.user.email),
                                       question_id=get.id, answer=x['ans'], post=post)
        else:
            return Response({"error":"failed"}, status= status.HTTP_400_BAD_REQUEST)
        return Response(request.data)


class PosterFoundQuestions(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     questions = Questions.objects.filter(question_type="adopter", type__type="found")
    #     data_dict = {}
    #     count = 0
    #     for question in questions:
    #         count +=1
    #         if question.answer_details is not None:
    #             options = [x for x in question.answer_details.split(',')]
    #         else:
    #             options = []
    #         data_dict[count] = {'question':question.question, 'type':question.answer_type,
    #                             'options':options}
    #     return Response(data_dict)

    def get(self, request):
        print(request.__dict__)
        type = Type.objects.get(content_type__model='poster', type='found')
        posts = Posts.objects.filter(user=UserProfile.objects.get(email=request.user.email))
        main_list = []
        for post in posts:
            answers = Answer.objects.filter(question__question_type="poster", question__type=type,
                                            user=UserProfile.objects.get(email=request.user.email), post_id=post.id)

            data_dict = {}
            data_dict['post_id'] = post.id
            details = []
            for answer in answers:
                details.append({'question': answer.question.question, 'type': answer.question.answer_type,
                                'answer': answer.answer})
            data_dict['details'] = details

            if len(data_dict['details']) == 0:
                print (data_dict)
                del data_dict['post_id']
            else:
                main_list.append(data_dict)
        return Response(main_list)

    def post(self, request):
        data = PosterOwnAnswerSerailizer(data=request.data, many=True)
        type = Type.objects.get(content_type__model='poster', type='found')
        post = Posts.objects.create(user=UserProfile.objects.get(email=request.user.email))
        if data.is_valid():
            for x in data.data:
                get, created = Questions.objects.get_or_create(question=x['ques'], answer_type=x["type"],
                                                               type=type, question_type="poster")
                if not created:
                   get = Questions.objects.get(question=x['ques'], answer_type=x["type"], type=type)
                Answer.objects.create(user=UserProfile.objects.get(email=request.user.email),
                                       question_id=get.id, answer=x['ans'], post_id=post.id)
        else:
            return Response({"error":"failed"}, status= status.HTTP_400_BAD_REQUEST)
        return Response(request.data)


class AdopterQuestions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        # answers = Answer.objects.filter(question__question_type="adopter", question__type=type,
        #                                   user=UserProfile.objects.get(email=request.user.email))
        # data_dict = {}
        # count = 0
        # for answer in answers:
        #     count +=1
        #     data_dict[count] = {'question':answer.question.question, 'type':answer.question.answer_type,
        #                         'answer':answer.answer}
        # return Response(data_dict)

        type = Type.objects.get(content_type__model='adopter', type='interested')
        posts = Posts.objects.filter(user=UserProfile.objects.get(email=request.user.email))
        main_list = []
        for post in posts:
            answers = Answer.objects.filter(question__question_type="adopter", question__type=type,
                                            user=UserProfile.objects.get(email=request.user.email), post_id=post.id)

            data_dict = {}
            data_dict['post_id'] = post.id
            details = []
            for answer in answers:
                details.append({'question': answer.question.question, 'type': answer.question.answer_type,
                                'answer': answer.answer})
            data_dict['details'] = details

            if len(data_dict['details']) == 0:
                del data_dict['post_id']
            else:
                main_list.append(data_dict)
        return Response(main_list)

    def post(self, request, id):
        data = AdopterQuestionsSerailizer(data=request.data, many=True)
        type = Type.objects.get(content_type__model='adopter', type='interested')
        post = Posts.objects.get(id=id)

        if data.is_valid():
            for x in data.data:
                get, created = Questions.objects.get_or_create(question=x['ques'], answer_type=x["type"],
                                                               type=type, question_type="adopter")
                if not created:
                   get = Questions.objects.get(question=x['ques'], answer_type=x["type"], type=type)
                Answer.objects.create(user=UserProfile.objects.get(email=request.user.email),
                                       question_id=get.id, answer=x['ans'], post=post)
        else:
            return Response({"error":"failed"}, status= status.HTTP_400_BAD_REQUEST)
        return Response(request.data)





