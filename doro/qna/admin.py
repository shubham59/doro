from django.contrib import admin
from .models import Questions, Answer
# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'type', 'answer_type', 'question_type', 'answer_details']
    fields = ['question', 'type', 'answer_type', 'question_type', 'answer_details']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'answer', 'question']


admin.site.register(Questions, QuestionsAdmin)