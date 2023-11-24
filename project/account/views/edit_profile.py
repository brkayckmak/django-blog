from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import edit_profile_form

@login_required(login_url="/")
def edit_profile(request):
    if request.method == "POST":
        form = edit_profile_form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile edited.")
            return redirect("edit-profile")
    else:
        form = edit_profile_form(instance=request.user)
    
    context = {"form": form}

    return render(request, "pages/edit-profile.html", context=context)