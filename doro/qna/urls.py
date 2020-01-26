from django.urls import path
from .views import PosterFoundQuestions, PosterOwnQuestions, AdopterQuestions


urlpatterns = [
    path(r'poster/own/', PosterOwnQuestions.as_view()),
    path('poster/found/', PosterFoundQuestions.as_view()),
    path('adopter/<int:id>/', AdopterQuestions.as_view()),
]
