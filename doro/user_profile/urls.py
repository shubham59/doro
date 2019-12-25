from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.user_register),
    path('verify/', views.verify),
    path('profile/', views.UpdateUserProfile.as_view()),
]
