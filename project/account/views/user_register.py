from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import user_register_form
from django.contrib.auth import login, authenticate

def user_register(request):
    if request.method == "POST":
        form = user_register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("mainpage")
    else:
        form = user_register_form()
    
    context = {"form": form}

    return render(request, "pages/register.html", context=context)