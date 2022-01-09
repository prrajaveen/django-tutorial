from django.core import validators
from django import forms
from django.forms.widgets import CheckboxInput

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should start with s')

class StudentRegistration(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(error_messages={'required':'Enter your Email'},widget=forms.EmailInput( attrs={'class':'form-control'}))
    password=forms.CharField(error_messages={'required':'Enter your Password'},widget=forms.PasswordInput( attrs={'class':'form-control'}))
    
    
    