from typing import Any
from django.contrib.auth.decorators import login_required
from django.db import models
from blog.models import writings_model
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy #for success url
from django.contrib.auth.mixins import LoginRequiredMixin

#Delete Class View
class delete_writing_delete_view(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    template_name = "pages/delete_writing_confirmation.html" #confirmation of deleting
    success_url = reverse_lazy("my_writings")

    def get_queryset(self):
        writing = writings_model.objects.all().filter(slug=self.kwargs["slug"], writer=self.request.user)
        return writing

#Normal View
# @login_required(login_url="/")
# def delete_writing(request, slug):
#     writing_to_delete = get_object_or_404(writings_model, slug=slug, writer=request.user)
#     writing_to_delete.delete()
#     return redirect("my_writings")