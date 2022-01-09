from typing import List

from django.views.generic.base import TemplateView
from myapplication.models import Student
from django.db import models
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm,NewContect


class StudentFormView(FormView):
    template_name='myapplication/home.html'
    form_class=ContactForm
    success_url='/thankyou/'
    def form_valid(self,form):
        print(form.cleaned_data['name'])
        return super().form_valid(form)
    
    # def get_context_data(self,*args,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['form2']=NewContect()
    #     return context


class ThankView(TemplateView):
    template_name='myapplication/thankyou.html'






