from myapplication.models import Student
from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.

# <--------------- defalult view of listview-------------------->
#==>Template name should be modelname_list.html
#==>During template rendering use modelname_list or object_list
#===> By default it will set template_name_sufix='_list'
class Home(ListView):
    model = Student

# <---------------Custom view of ListView---------------------->
#===>define template_name=example/example.html
#====> we can change template_name_sufix='_get'
class StudentInfo(ListView):
    model=Student
    template_name_suffix='_get'
    ordering=['name']

# <------------ Custom template name in ListView --------------->

class StudentUsingCustomTemplateName(ListView):
    model=Student
    template_name='myapplication/home.html'
    context_object_name='students'

    def get_queryset(self):
        return Student.objects.filter(course='python')
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['fresher']=Student.objects.all().order_by('name')
        return context
#<=========== Important concept ==============>
    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'sonam':
    #         template_name='myapplication/sonam.html'
    #     elif self.request.user.is_superuser:
    #         template_name='myapplication/superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name='myapplication/staff.html'
    #     else:
    #         template_name=self.template_name
    #     return [template_name]

    
