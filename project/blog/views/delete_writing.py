from django.contrib.auth.decorators import login_required
from blog.models import writings_model
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url="/")
def delete_writing(request, slug):
    writing_to_delete = get_object_or_404(writings_model, slug=slug, writer=request.user)
    writing_to_delete.delete()
    return redirect("my_writings")