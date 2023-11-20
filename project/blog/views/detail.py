from django.shortcuts import render, get_object_or_404
from blog.models import writings_model

def detail(request, slug):
    writing = get_object_or_404(writings_model, slug=slug)
    comments = writing.comments.all()
    context = {"writing": writing, "comments": comments}
    return render(request, "pages/detail.html", context=context)