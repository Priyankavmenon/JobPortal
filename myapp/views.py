from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Welcomepage(TemplateView):
    template_name="welcome.html"