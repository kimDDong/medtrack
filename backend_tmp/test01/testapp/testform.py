from django import forms
from .models import Bookmark

# Create your models here.


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)

class gaip(forms.Form):
    user_id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    social_number = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    preferred_hospital = forms.CharField(max_length=100)

class login(forms.Form) :
    user_id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class addMedi(forms.Form):
    name = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)

class set(forms.Form):
    font_size = forms.IntegerField()