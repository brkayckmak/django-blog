from django.contrib.auth.decorators import login_required
from blog.models import comment_model
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required(login_url="/")
def delete_comment(request, id):
    comment = get_object_or_404(comment_model, id=id)
    if comment.writer == request.user or comment.writing.writer == request.user:
        comment.delete()
        messages.success(request, "Comment deleted.")
        return redirect("detail", slug=comment.writing.slug)
    return redirect("mainpage")