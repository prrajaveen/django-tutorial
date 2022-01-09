from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='your password',widget=forms.PasswordInput(attrs={'class':'raja'}))
    password2=forms.CharField(label='Password (again)',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
