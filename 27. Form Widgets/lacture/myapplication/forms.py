from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput

class StudentRegistration(forms.Form):
    # name=forms.CharField(label='Your Name',label_suffix=' ',initial='Anil kumar',required=False,disabled=True,help_text='Limit 70 character')
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))
    textarea=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    checkbox=forms.CharField(widget=forms.CheckboxInput())
    file=forms.CharField(widget=forms.FileInput(attrs={'class':'form-control'}))
    newfile=forms.CharField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
 