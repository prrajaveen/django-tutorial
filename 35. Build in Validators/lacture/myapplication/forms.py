from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import fields, models

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'
    