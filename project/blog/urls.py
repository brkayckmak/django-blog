from django.urls import path
from blog.views import contact, mainpage, category

urlpatterns = [
    path("", mainpage, name="mainpage"),
    path("contact/", contact, name="contact"),
    path("category/<slug:category_slug>", category, name="category")
]
