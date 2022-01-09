from django.core import validators
from django import forms
from django.forms.widgets import CheckboxInput

class StudentRegistration(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput( attrs={'class':'form-control'}))

    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('name must be 4 character')

    def clean(self):
        valemail=self.cleaned_data['email']
        print(valemail)
        if len(valemail)<4:
            raise forms.ValidationError('email must be 4 character')
    
    