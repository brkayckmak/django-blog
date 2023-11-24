from django.shortcuts import render, get_object_or_404
from blog.models import category_model
from django.core.paginator import Paginator

def category(request, category_slug):
    category = get_object_or_404(category_model, slug=category_slug)
    writings = category.writing.order_by("-id")
    
    page = request.GET.get("page")
    paginator = Paginator(writings, 2)
    
    context = {"writings": paginator.get_page(page),
               "category_name": category.name}
    return render(request, "pages/category.html", context=context)