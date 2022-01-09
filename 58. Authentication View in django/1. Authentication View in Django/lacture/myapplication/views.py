from django.shortcuts import render
from django.contrib.auth import urls
from django.views.generic import TemplateView
# Create your views here.

class Profile(TemplateView):
    template_name='myapplication/profile.html'