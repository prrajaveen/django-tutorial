from django.core import validators
from django import forms
from django.forms.widgets import CheckboxInput

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should start with s')

class StudentRegistration(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput( attrs={'class':'form-control'}))
    rpassword=forms.CharField(label='Password (again)',widget=forms.PasswordInput( attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        valpwd=cleaned_data.get('password')
        valrpwd=cleaned_data.get('rpassword')
        if valpwd!=valrpwd:
            raise forms.ValidationError('password do not match')
    
    