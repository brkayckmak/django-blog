from django.contrib import admin
from blog.models import category_model, writings_model

admin.site.register(category_model)

class writings_admin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "creation_date", "update_date")

admin.site.register(writings_model, writings_admin)