from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def my_writings(request):
    writings = request.user.writings.order_by("-id")
    
    page = request.GET.get("page")
    paginator = Paginator(writings, 1)
    
    context = {"writings": paginator.get_page(page)}
    return render(request, "pages/my_writings.html", context=context)