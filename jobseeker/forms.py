from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Student

class ARegister(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password1","password2","email"]
# class Login(forms.Form):
#     username=forms.CharField()
#     password=forms.CharField()
class Studentprofile(forms.ModelForm):
    class Meta:
        model=Student
        exclude=('user',)
        fields='__all__'