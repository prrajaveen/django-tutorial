from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class Profile(TemplateView):
    template_name='myapplication/profile.html'

