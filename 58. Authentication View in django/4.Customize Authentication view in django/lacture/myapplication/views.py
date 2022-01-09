from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView
from myapplication.forms import LoginForm
# Create your views here.

class Profile(TemplateView):
    template_name='myapplication/profile.html'

class MyLoginView(LoginView):
    template_name='myapplication/login.html'
    authentication_form=LoginForm
    

