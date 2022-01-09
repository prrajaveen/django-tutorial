from django import forms
from django.forms.fields import EmailField

class StudentRegistration(forms.Form):
    name=forms.CharField(initial='sonam',help_text='is field me 30 character likh sakete hai', required=False)
 