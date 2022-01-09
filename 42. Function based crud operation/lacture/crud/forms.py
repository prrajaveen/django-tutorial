from django import forms
from django.forms import ModelForm, fields, models, widgets
from crud.models import Student

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=['name','email','password']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})}
        label={'name':'Enter Your Name','email':'Enter your email','password':'Enter your Password'}
