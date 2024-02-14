from django import forms
from myapp.models import Category,Job

class HrLoginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class Categoryform(forms.ModelForm):
    class Meta:
        model= Category
        fields= ["name"]
class Jobform(forms.ModelForm):
    class Meta:
        model= Job
        #exclude=('salary',)#given if we want to exclude any particular field
        fields= "__all__"
