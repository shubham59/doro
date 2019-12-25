from django.urls import path
from .views import AdopterOwnQuestions, AdopterFoundQuestions


urlpatterns = [
    path(r'adopter/own/', AdopterOwnQuestions.as_view()),
    path('adopter/found/', AdopterFoundQuestions.as_view()),
]
