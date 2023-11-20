from django.urls import path
from blog.views import contact, mainpage, category, my_writings, detail

urlpatterns = [
    path("", mainpage, name="mainpage"),
    path("contact/", contact, name="contact"),
    path("category/<slug:category_slug>", category, name="category"),
    path("my_writings", my_writings, name="my_writings"),
    path("detail/<slug:slug>", detail, name="detail"),
]
