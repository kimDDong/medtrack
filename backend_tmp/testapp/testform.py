from django import forms
from .models import Bookmark

# Create your models here.


#이게 모델 (db?)
class BookForm(forms.Form):
    #이 내용이 저장되는 (입력할 수 있는) db가 만들어짐
    name = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)

class gaip(forms.Form):
    #이 내용이 저장되는 (입력할 수 있는) db가 만들어짐
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

