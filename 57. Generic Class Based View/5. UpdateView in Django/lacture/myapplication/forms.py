from django import forms
from django.forms import fields
from django.forms.forms import Form
from django.utils.regex_helper import contains
from .models import Student
class ContactForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','roll','course']

class NewContect(forms.Form):
    name=forms.CharField(widget=forms.TextInput())