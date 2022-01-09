from django.core import validators
from django import forms
from django.forms.widgets import CheckboxInput

class StudentRegistration(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput( attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


    def clean_name(self):
        valname=self.cleaned_data['name']
        print(valname)
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than or equeal to 4 character')
        return valname
    
    def clean_email(self):
        valname=self.cleaned_data['email']
        print(valname)
        if '@' not in valname:
            raise forms.ValidationError('@ not present in your email')
        return valname
    
    def clean_email(self):
        valname=self.cleaned_data['email']
        if not valname.endswith('.com'):
            raise forms.ValidationError('.com is not present in your email')   

