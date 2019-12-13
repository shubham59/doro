from django.contrib import admin
from .models import *
# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'type']
    fields = ['question', 'type']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'answer', 'question']


admin.site.register(Questions, QuestionsAdmin)