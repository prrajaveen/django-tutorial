import myapplication
from typing import List

from django.views.generic.base import TemplateView
from myapplication.models import Student
from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import ContactForm,NewContect
from django import forms


# class StudentFormView(CreateView):
#     model=Student
#     template_name='myapplication/home.html'
#     fields=['name','roll','course']
#     # success_url='/detail/'
#     def get_form(self):
#         form=super().get_form()
#         form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass','placeholder':'Enter your name'})
#         form.fields['roll'].widget=forms.TextInput(attrs={'class':'myclass'})
#         form.fields['course'].widget=forms.TextInput(attrs={'class':'myclass'})
#         return form


class StudentFormView(CreateView):
    form_class=ContactForm
    template_name='myapplication/home.html'




class StudentDetailView(DetailView):
    model=Student


class ThankView(TemplateView):
    template_name='myapplication/thankyou.html'






