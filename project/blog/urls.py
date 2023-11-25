from django.urls import path
from blog.views import contact, mainpage, category_list_view, my_writings, detail_view, add_writing, update_writing, delete_writing_delete_view, delete_comment

urlpatterns = [
    path("", mainpage, name="mainpage"),
    path("contact/", contact, name="contact"),
    path("category/<slug:category_slug>", category_list_view.as_view(), name="category"),
    path("my_writings", my_writings, name="my_writings"),
    path("detail/<slug:slug>", detail_view.as_view(), name="detail"),
    path("add-writing", add_writing, name="add-writing"),
    path("update-writing/<slug:slug>", update_writing, name="update-writing"),
    path("delete-writing/<slug:slug>", delete_writing_delete_view.as_view(), name="delete-writing"),
    path("delete-comment/<int:id>", delete_comment, name="delete-comment"),

]
