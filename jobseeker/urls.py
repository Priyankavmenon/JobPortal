from django.urls import path
from jobseeker import views

urlpatterns=[
    path("register",views.Regview.as_view(),name="register"),
    path("student",views.Student_home.as_view(),name="studentindex"),
    path("studprofile",views.Studentprofileview.as_view(),name="studentprofile"),
    path("viewprofile/<int:pk>",views.Viewprofile.as_view(),name="viewprofile"),
    path("editprofile/<int:pk>",views.Update_profile.as_view(),name="update"),
    path("jobview<int:pk>",views.Jobdetail.as_view(),name="jobview"),
    path("job_apply<int:pk>",views.Job_apply.as_view(),name="jobapply"),
    path("applied",views.Applied.as_view(),name="applied"),
    path("applydel<int:pk>",views.Job_applieddelte.as_view(),name="applydel")
    ]