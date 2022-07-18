from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "active")
    list_editable = ("active",)


admin.site.register(Account, AccountAdmin)
