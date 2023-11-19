from django.shortcuts import render

def mainpage(request):
    context = {"name": "Berkay Cakmak"}
    return render(request, "pages/mainpage.html", context=context)