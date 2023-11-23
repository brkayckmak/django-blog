from django import forms
from blog.models import writings_model

class update_writing_model_form(forms.ModelForm):
    class Meta:
        model = writings_model
        exclude = ("writer", "slug")