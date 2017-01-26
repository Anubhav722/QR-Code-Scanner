from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    exclude = ['qr_code', 'auth_token']

admin.site.register(UserProfile, UserProfileAdmin)
