from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'last_name', 'avatar']


admin.site.register(User, UserAdmin)
