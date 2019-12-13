from django.contrib import admin
from .models import *
# Register your models here.


class AdopterAdmin(admin.ModelAdmin):
    list_display = ['user', 'type']


admin.site.register(Adopter, AdopterAdmin)