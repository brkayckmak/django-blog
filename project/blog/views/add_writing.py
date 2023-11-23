from django.shortcuts import render, redirect
from blog.forms import add_writing_model_form
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def add_writing(request):
    form = add_writing_model_form(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        writing = form.save(commit=False) #take data but don't save to db.
        writing.writer = request.user
        writing.save()

        form.save_m2m() #save writing to related category (m2m field)
        return redirect("detail", slug=writing.slug)
    context = {"form": form}

    return render(request, "pages/add-writing.html", context=context)