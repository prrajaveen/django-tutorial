from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required,name='dispatch')
class Profile(TemplateView):
    template_name='myapplication/profile.html'
    
    # @method_decorator(login_required)
    # def dispatch(self,*args,**kwargs):
    #     return super().dispatch(*args,**kwargs)

@method_decorator(staff_member_required,name='dispatch')
class About(TemplateView):
    template_name='myapplication/about.html'

    # @method_decorator(staff_member_required)
    # def dispatch(self,*args,**kwargs):
    #     return super().dispatch(*args,**kwargs)

