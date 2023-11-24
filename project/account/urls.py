from django.urls import path
from account.views import log_out, change_passw

urlpatterns = [
    path("logout", log_out, name="logout"),
    path("change-password", change_passw, name="change-password")
]