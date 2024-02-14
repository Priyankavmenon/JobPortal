from django.urls import path
from hr import views

urlpatterns=[
    path("",views.Loginview.as_view(),name="signin"),
    path("index",views.Dashboard.as_view(),name="index"),
    path("logout",views.Signout.as_view(),name="signout"),
    path("category",views.Addcategory.as_view(),name="category"),
    path("delete/<int:pk>",views.Deletecategory.as_view(),name="delete"),
    path("job",views.Addjob.as_view(),name="job"),
    path("listjob",views.Listjob.as_view(),name="listjob"),
    path("deletejob/<int:pk>",views.Deletejob.as_view(),name="deletejob"),
    path("singlejob/<int:pk>",views.Viewsortedjobs.as_view(),name="singlejob"),
    path("jobedit/<int:pk>",views.Jobupdate.as_view(),name="edit"),
    path("viewapplied",views.Viewapplied.as_view(),name="viewapplied"),
    path("signout/",views.Signout.as_view(),name='signout')

             ]