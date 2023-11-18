from django.contrib import admin
from blog.models import category_model, writings_model, comment_model, contact_model

admin.site.register(category_model)

class writings_admin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "creation_date", "update_date")

admin.site.register(writings_model, writings_admin)

class comments_admin(admin.ModelAdmin):
    search_fields = ("writer__username", "writing__id")
    list_display = ("writer", "creation_date", "update_date")

admin.site.register(comment_model, comments_admin)

class contact_admin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "creation_date")

admin.site.register(contact_model, contact_admin)