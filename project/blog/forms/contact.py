from django import forms

class contact_form(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    name = forms.CharField(label="Name", max_length=20)
    message = forms.CharField(label="Message", widget=forms.Textarea)