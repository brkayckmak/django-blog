from django.shortcuts import render, get_object_or_404, redirect
from blog.models import writings_model
from blog.forms import add_comment_model_form
from django.views import View
import logging

logger = logging.getLogger("read_writing")
#Class Type View
class detail_view(View):
    http_method_names = ["get", "post"] #This view will support get and post requests.
    add_comment_form = add_comment_model_form

    def get(self, request, slug):
        writing = get_object_or_404(writings_model, slug=slug)
        comments = writing.comments.all()
        
        if request.user.is_authenticated:
            logger.info("writing read: " + request.user.username)

        context = {"writing": writing, "comments": comments, "add_comment_form": self.add_comment_form}
        return render(request, "pages/detail.html", context=context)
    
    def post(self, request, slug):
        writing = get_object_or_404(writings_model, slug=slug)
        add_comment_form = self.add_comment_form(data=request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.writer = request.user
            comment.writing = writing
            comment.save()
        return redirect("detail", slug=slug)


#Normal View
# def detail(request, slug):
#     writing = get_object_or_404(writings_model, slug=slug)
#     comments = writing.comments.all()

#     if request.method == "POST":
#         add_comment_form = add_comment_model_form(data=request.POST)
#         if add_comment_form.is_valid():
#             comment = add_comment_form.save(commit=False)
#             comment.writer = request.user
#             comment.writing = writing
#             comment.save()
    
#     add_comment_form = add_comment_model_form()

#     context = {"writing": writing, "comments": comments, "add_comment_form": add_comment_form}
#     return render(request, "pages/detail.html", context=context)