from django.views.generic import DetailView
from account.models import custom_user_model
from django.shortcuts import get_object_or_404

class profile_detail_view(DetailView):
    template_name = "pages/profile.html"
    context_object_name = "profile"
    
    def get_object(self):
        return  get_object_or_404(custom_user_model, username=self.kwargs["username"])