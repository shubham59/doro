from django.contrib import admin
from .models import *
# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    fields = ['content_type', 'type']
    list_display = ['content_type', 'type']


class PosterAdmin(admin.ModelAdmin):
    fields = ['user', 'type']
    list_display =  ['user', 'type']


admin.site.register(Type, TypeAdmin)
admin.site.register(Poster, PosterAdmin)