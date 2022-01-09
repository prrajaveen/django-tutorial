from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django import forms
from django.db.models import fields

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='your password',widget=forms.PasswordInput(attrs={'class':'raja'}))
    password2=forms.CharField(label='Password (again)',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        label={'email':'Email'}
