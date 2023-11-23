from django import forms
from blog.models import comment_model

class add_comment_model_form(forms.ModelForm):
    class Meta:
        model = comment_model
        fields = ("comment",)