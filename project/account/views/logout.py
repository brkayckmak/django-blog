from django.contrib.auth import logout
from django.shortcuts import redirect

def log_out(request):
    logout(request)
    return redirect("mainpage")