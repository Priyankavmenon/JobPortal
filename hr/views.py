from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,DetailView,UpdateView
from hr.forms import HrLoginform,Jobform
from django.contrib import messages
from hr.forms import HrLoginform,Categoryform
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from myapp.models import Category,Job,Application
class Loginview(FormView):
    template_name="login.html"
    form_class=HrLoginform
    def post(self, request,*args,**kwargs):

        lform=HrLoginform(request.POST)
        if lform.is_valid():
            username=lform.cleaned_data.get("username")
            password=lform.cleaned_data.get("password")
            obj=authenticate(request,username=username,password=password)
            if obj:
                login(request,obj)
                if request.user.is_superuser:
                    messages.success(request,"Login successful")
                    return redirect("index")
                else:
                    return redirect("studentindex")
            else:
                messages.error(request,"Invalid credentials")
            return render(request,"login.html",{"lf":lform})

class Dashboard(TemplateView):
    template_name="index.html"
class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
class Addcategory(CreateView,ListView):# This covers both create  display
    template_name="category.html"
    form_class=Categoryform
    success_url=reverse_lazy("category")
    context_object_name="data"#this is instead of ORM data=models.objects.all()
    model=Category
class Deletecategory(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.get(id=id).delete()
        return redirect("category")
        
class Addjob(CreateView):    
    template_name="job.html"
    form_class=Jobform
    success_url=reverse_lazy("index")
    model=Job
   
    context_object_name="data"
class Listjob(ListView):  
     model=Job
     context_object_name="qs"
     template_name="listjob.html"
class Viewsortedjobs(View):
     def get(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            print(id)
            details=Job.objects.filter(category_id=id)
            return render(request,"singlejob.html",{"details":details})
class Deletejob(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Job.objects.get(id=id).delete()
        return redirect("listjob")
class Jobupdate(UpdateView):
    form_class=Jobform
    template_name="job_edit.html"
    model=Job
    success_url=reverse_lazy("index")

class Viewapplied(View):
    def get(self,request,*args,**kwargs):
        data=Application.objects.all()
        print(data)
        
        return render(request,"applied.html",{"data":data})

