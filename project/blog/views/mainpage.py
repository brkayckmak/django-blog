from django.shortcuts import render
from blog.models import writings_model
from django.core.paginator import Paginator

def mainpage(request):
    writings = writings_model.objects.order_by("-id")
    page = request.GET.get("page")

    paginator = Paginator(writings, 1)
    
    context = {"writings": paginator.get_page(page)}
    return render(request, "pages/mainpage.html", context=context)