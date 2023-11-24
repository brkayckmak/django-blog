from django.shortcuts import render
from blog.models import writings_model
from django.core.paginator import Paginator
from django.db.models import Q

def mainpage(request):
    search = request.GET.get("search")
    writings = writings_model.objects.order_by("-id")
    if search:
        writings = writings.filter(Q(title__icontains=search) | Q(content__icontains=search)).distinct()
    page = request.GET.get("page")

    paginator = Paginator(writings, 2)
    
    context = {"writings": paginator.get_page(page)}
    return render(request, "pages/mainpage.html", context=context)