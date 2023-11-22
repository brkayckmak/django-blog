from django.shortcuts import render, redirect
from blog.forms import contact_form
from blog.models import contact_model

def contact(request):
    form = contact_form()
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            model = contact_model()
            model.email = form.cleaned_data["email"]
            model.name = form.cleaned_data["name"]
            model.message = form.cleaned_data["message"]
            model.save()
            return redirect("mainpage")
    context = {"form": form}
    return render(request, "pages/contact.html", context=context)