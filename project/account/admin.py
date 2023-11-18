from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import custom_user_model

class custom_admin(UserAdmin):
    model = custom_user_model
    list_display = ("username", "email")
    fieldsets = UserAdmin.fieldsets + (("Avatar Change", {"fields":["avatar"]}),)

admin.site.register(custom_user_model, custom_admin)