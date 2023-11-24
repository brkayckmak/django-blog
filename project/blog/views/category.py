from django.shortcuts import render, get_object_or_404
from blog.models import category_model
from django.core.paginator import Paginator
from django.views.generic import ListView

#Class List View
class category_list_view(ListView):
    template_name = "pages/category.html"
    model = category_model
    context_object_name = "writings"
    paginate_by = 2

    def get_queryset(self):
       category = get_object_or_404(category_model, slug=self.kwargs["category_slug"])
       return category.writing.all().order_by("-id")


#Normal View
# def category(request, category_slug):
#     category = get_object_or_404(category_model, slug=category_slug)
#     writings = category.writing.order_by("-id")
    
#     page = request.GET.get("page")
#     paginator = Paginator(writings, 2)
    
#     context = {"writings": paginator.get_page(page),
#                "category_name": category.name}
#     return render(request, "pages/category.html", context=context)