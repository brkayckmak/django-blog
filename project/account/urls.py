from django.urls import path
from account.views import log_out, change_passw, edit_profile, user_register

urlpatterns = [
    path("logout", log_out, name="logout"),
    path("change-password", change_passw, name="change-password"),
    path("edit-profile", edit_profile, name="edit-profile"),
    path("register", user_register, name="register")
]