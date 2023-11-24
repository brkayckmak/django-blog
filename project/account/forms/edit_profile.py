from django.contrib.auth.forms import UserChangeForm
from account.models import custom_user_model

class edit_profile_form(UserChangeForm):
    password = None
    class Meta:
        model = custom_user_model
        fields = ("email", "first_name", "last_name", "avatar")