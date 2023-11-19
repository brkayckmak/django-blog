from django.urls import path
from blog.views import contact, mainpage

urlpatterns = [
    path("", mainpage, name="mainpage"),
    path("contact/", contact, name="contact"),
]
