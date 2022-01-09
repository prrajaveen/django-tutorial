from django.core import validators
from django import forms
from django.db import models
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import CheckboxInput
from myapplication.models import User



class StudentRegistration(forms.ModelForm):
    # name=forms.CharField(max_length=50,required=False)
    class Meta:
        model=User
        fields=['name','email','password']
        # fields='__all__'
        # exclude=['name']
        labels={'name':'Enter Name','password':'Enter password','email':'Enter Email'}
        help_text={'name':'name should be 4 character','email':'email include @0','password':'password should be uppercase'}
        error_messages={'name':{'required':'Nam likhna jaroori hai'},'email':{'required':'email likhna jaroori hai'}}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'password':forms.PasswordInput(attrs={'class':'form-control'})}
        
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields='__all__'
        

    
    