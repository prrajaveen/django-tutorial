import myapplication
from typing import List

from django.views.generic.base import TemplateView
from myapplication.models import Student
from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm,NewContect
from django import forms
from django.contrib import messages
from django.core import exceptions


class StudentCreateView(CreateView):
    form_class=ContactForm
    template_name='myapplication/home.html'
    success_url='/thankyou/'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['students']=Student.objects.all()
        return context

class StudentThankTemplateView(TemplateView):
    template_name='myapplication/thankyou.html'

# class StudentUpdateView(UpdateView):
#     template_name='myapplication/update.html'
#     model=Student
#     fields=['name','roll','course']
#     success_url='/thankyou/'

class StudentUpdateView(SuccessMessageMixin,UpdateView):
    model=Student
    form_class=ContactForm
    template_name='myapplication/update.html'
    success_message='Your data has been secussfully updated'
    success_url='/thankyou/'
    

class StudentDeteteView(SuccessMessageMixin,DeleteView):
    model=Student
    template_name='myapplication/delete.html'
    success_message='Your data has been secussfully deleted'
    success_url='/create/'

    def get_object(self):
        qs = super(StudentDeteteView, self).get_object()
        if self.request.user.has_perm('edit_lecture', qs):
            return qs
        else:
            raise exceptions.PermissionDenied
    

    



