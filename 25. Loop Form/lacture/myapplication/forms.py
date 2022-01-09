from django import forms
from django.forms.fields import EmailField

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    city=forms.CharField()
    key=forms.CharField(widget=forms.HiddenInput())
 