from django.shortcuts import render, get_object_or_404
from blog.models import writings_model
from blog.forms import add_comment_model_form

def detail(request, slug):
    writing = get_object_or_404(writings_model, slug=slug)
    comments = writing.comments.all()

    if request.method == "POST":
        add_comment_form = add_comment_model_form(data=request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.writer = request.user
            comment.writing = writing
            comment.save()
    
    add_comment_form = add_comment_model_form()

    context = {"writing": writing, "comments": comments, "add_comment_form": add_comment_form}
    return render(request, "pages/detail.html", context=context)