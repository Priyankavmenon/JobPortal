from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Job(models.Model):
    jobname=models.CharField(max_length=200)
    companyname=models.CharField(max_length=200)
    experience=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    qualification=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    poster=models.ImageField(upload_to='poster',null=True)
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.jobname
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING,related_name="profile",null=True)#to check wether the user has created a profile
   
    age=age=models.PositiveIntegerField()
    options=(("male","male"),("female","female"))
    gender=models.CharField(max_length=20,choices=options,default="male")
    qualification=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    contact=models.CharField(max_length=20)
    resume=models.FileField(upload_to="files",null=True)
    experience=models.CharField(max_length=200)
    # def __str__(self):
    #     return self.user
class Application(models.Model):
    """A model for HR to check the job applicants and their details"""
    jobs=models.ForeignKey(Job,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    applicantdetails=models.OneToOneField(Student,on_delete=models.CASCADE,null=True)
    options=(("pending","pending"),("rejected","rejected"),("processing","processing"))
    status=models.CharField(max_length=20,choices=options,default="pending")