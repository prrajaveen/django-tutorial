from django import forms
from django.forms.fields import EmailField

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    first_name=forms.CharField()