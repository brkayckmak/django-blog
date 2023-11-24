from django.contrib.auth.forms import UserCreationForm
from account.models import custom_user_model

class user_register_form(UserCreationForm):
    class Meta:
        model = custom_user_model
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")