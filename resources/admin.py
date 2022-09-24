from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'dob', 'address', 'created_date']

admin.site.register(UserProfile, UserProfileAdmin)
