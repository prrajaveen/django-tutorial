from django import forms
from django.forms.fields import EmailField

class StudentRegistration(forms.Form):
    name=forms.CharField(label='Your Name',label_suffix=' ',initial='Anil kumar',required=False,disabled=True,help_text='Limit 70 character')
 
 