from typing import Any
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import update_writing_model_form
from django.contrib.auth.decorators import login_required
from blog.models import writings_model
from django.views.generic import UpdateView
from django.urls import reverse

#Update Class View
class update_writing_update_view(UpdateView):
    template_name = "pages/update-writing.html"
    fields = ("image", "title", "content", "categories")

    def get_object(self):
        writing = get_object_or_404(writings_model, slug=self.kwargs["slug"], writer=self.request.user)
        return writing
    
    def get_success_url(self):
        return reverse("detail", kwargs={"slug": self.get_object().slug})
        
#Normal View
# @login_required(login_url="/")
# def update_writing(request, slug):
#     writing = get_object_or_404(writings_model, slug=slug, writer=request.user)
#     form = update_writing_model_form(request.POST or None, files=request.FILES or None, instance=writing)
#     if form.is_valid():
#         form.save()
#         return redirect("detail", slug=writing.slug)
    
#     context = {"form":form}

#     return render(request, "pages/update-writing.html", context=context)