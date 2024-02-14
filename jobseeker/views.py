from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,UpdateView,ListView,DetailView
from jobseeker.forms import ARegister
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from jobseeker.forms import Studentprofile
from myapp.models import Student,Job,Application
from django.utils.decorators import method_decorator

def signinreqd(cls):
    def wrapper(request,*args,**kwargs):
        if  not request.user.is_authenticated:
            return redirect("signin")
        else:
            return cls(request,*args,**kwargs)
    return wrapper



class Regview(CreateView):

    
    template_name="jobseeker/register.html"
    form_class=ARegister
    model=User
    success_url=reverse_lazy("hr/signin")
# class Signinview(View):
#     def get(self,request,*args,**kwargs):
#         form=Login
#         return render(request,"jobseeker/index.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         form=Login(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password")
#             obj=authenticate(request,username=username,password=password)
#             if obj:
#                 login(request,obj)
#                 messages.success(request,"Login successful")
#             else:
#                 messages.error(request,"Invalid credentials")
#                 return redirect("login")
#         return redirect("category")
@method_decorator(signinreqd,name="dispatch")    
class Student_home(ListView):
    template_name="jobseeker/index.html"
    model=Job
    context_object_name="job"
@method_decorator(signinreqd,name="dispatch")
class Studentprofileview(CreateView):  
    
    form_class=Studentprofile
    template_name="jobseeker/profile.html"
    model=Student
    success_url=reverse_lazy("job")
    # def post(self,request,*args,**kwargs):        
    #     form=Studentprofile(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #     else:
    #         redirect("studentprofile")
    #     return redirect("studentprofile")   
    def form_valid(self, form: BaseModelForm):#to pass instance into a form we can use this function
        form.instance.user=self.request.user
        return super().form_valid(form) #super() gets data from parent class which is User
@method_decorator(signinreqd,name="dispatch")
class Viewprofile(DetailView):
    
    template_name="jobseeker/profileview.html"
    model=Student
    context_object_name="data"
    success_url=reverse_lazy("viewprofile")
    # def get(self,request,*args,**kwargs):
        # id=kwargs.get("pk")
        # data=Student.objects.get(id=id)
        # user=request.user
        # data=Student.objects.filter(user=user)
        # print(data)
    
        # return render(request,"jobseeker/profileview.html",{"data":data})
    
    # form_class=Studentprofile
    # template_name="jobseeker/profileview.html"
    # model=Student
    # context_object_name="profile"
@method_decorator(signinreqd,name="dispatch")
class Update_profile(UpdateView):
    form_class=Studentprofile
    template_name="jobseeker/profile_update.html"
    model=Student
    success_url=reverse_lazy("register")
# class ABEABAIACB

# class Listjob(ListView):    
#     template_name="jobseeker/index.html"
#     model=Job
#     context_object_name="job"
@method_decorator(signinreqd,name="dispatch")
class Jobdetail(DetailView):
    template_name="jobseeker/jobdetail.html"
    model=Job
    context_object_name="jobview"
@method_decorator(signinreqd,name="dispatch")
class Job_apply(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Job.objects.get(id=id)
        data2=Student.objects.get(user=request.user)
        
        Application.objects.create(jobs=data,student=request.user,applicantdetails=data2)
        return redirect("studentindex")

@method_decorator(signinreqd,name="dispatch")
class Applied(View):
    def get(self,request,*args,**kwargs):
        data=Application.objects.filter(student=request.user)
        
        # print(data)
       
        return render(request,"jobseeker/jobapplied.html",{"data":data})
class Job_applieddelte(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Application.objects.get(id=id).delete()
        return redirect("studentindex")
