from django.core import validators
from django import forms
from django.forms.widgets import CheckboxInput

class StudentRegistration(forms.Form):
    name=forms.CharField(required=True,error_messages={'required':'Plese enter your name'})
    agree=forms.BooleanField(label='agree',error_messages={'required':'plese agree the condition'},widget=CheckboxInput())
    price=forms.DecimalField(label='Price',min_value=400,max_digits=5)

