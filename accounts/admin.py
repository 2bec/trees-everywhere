from django.contrib import admin

from .models import Account


class AccountInline(admin.TabularInline):
    model = Account.users.through
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "active")
    list_editable = ("active",)


admin.site.register(Account, AccountAdmin)
