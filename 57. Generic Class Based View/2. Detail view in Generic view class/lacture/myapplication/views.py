from typing import List
from myapplication.models import Student
from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

# <--------------- defalult view of listview-------------------->
#==>Template name should be modelname_list.html
#==>During template rendering use modelname_detail or object_list
#===> By default it will set template_name_sufix='_detail'
# class Home(D):
#     model = Student

# <---------------Custom view of ListView---------------------->
#===>define template_name=example/example.html
#====> we can change template_name_sufix='_get'

class StudentDetailView(DetailView):
    model=Student
    # template_name='myapplication/home.html'
    # context_object_name='stu'
    # pk_url_kwarg='id'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['students']=Student.objects.all()
        return context

class StudentListView(ListView):
    model=Student
    
