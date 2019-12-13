from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user_name', 'mobile', 'email']
    list_display = ['user_name', 'mobile', 'email']


admin.site.register(UserProfile, UserProfileAdmin)