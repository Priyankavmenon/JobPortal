from django.contrib import admin

from myapp.models import Job,Category,Student
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Student)