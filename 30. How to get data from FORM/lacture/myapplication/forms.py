from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput

class StudentRegistration(forms.Form):
    # name=forms.CharField(label='Your Name',label_suffix=' ',initial='Anil kumar',required=False,disabled=True,help_text='Limit 70 character')
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
 