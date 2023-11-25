from django.shortcuts import render, redirect
from blog.forms import add_writing_model_form
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from blog.models import writings_model
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Create Class View
class add_writing_create_view(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    template_name = "pages/add-writing.html"
    model = writings_model
    fields = ("title", "image", "content", "categories")

    def get_success_url(self):
        return reverse("detail", kwargs={"slug": self.object.slug})
     
    def form_valid(self, form):
        writing = form.save(commit=False) #take data but don't save to db.
        writing.writer = self.request.user
        writing.save()

        form.save_m2m() #save writing to related category (m2m field)
        return super().form_valid(form)
    
#Normal View
# @login_required(login_url="/")
# def add_writing(request):
#     form = add_writing_model_form(request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         writing = form.save(commit=False) #take data but don't save to db.
#         writing.writer = request.user
#         writing.save()

#         form.save_m2m() #save writing to related category (m2m field)
#         return redirect("detail", slug=writing.slug)
#     context = {"form": form}

#     return render(request, "pages/add-writing.html", context=context)