from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import update_writing_model_form
from django.contrib.auth.decorators import login_required
from blog.models import writings_model

@login_required(login_url="/")
def update_writing(request, slug):
    writing = get_object_or_404(writings_model, slug=slug, writer=request.user)
    form = update_writing_model_form(request.POST or None, files=request.FILES or None, instance=writing)
    if form.is_valid():
        form.save()
        return redirect("detail", slug=writing.slug)
    
    context = {"form":form}

    return render(request, "pages/update-writing.html", context=context)