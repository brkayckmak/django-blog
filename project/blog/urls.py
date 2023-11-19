from django.urls import path
from blog.views import contact, mainpage

urlpatterns = [
    path("", mainpage),
    path("contact/", contact),
]
