from django import template
from blog.models import category_model

register = template.Library()

@register.simple_tag
def category_list():
    categories = category_model.objects.all()
    return categories