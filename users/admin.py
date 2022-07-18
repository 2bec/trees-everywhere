from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.admin import AccountInline

from .models import Profile, User


class CustomUserAdmin(UserAdmin):
    model = User

    inlines = (AccountInline,)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
