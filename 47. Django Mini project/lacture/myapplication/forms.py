from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, models, widgets
from myapplication.models import Blogpost,ContactForm

class BlogSignupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password (Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),}

class BlogLoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields=['title','desc']
        widgets={'title':forms.TextInput(attrs={'class':'form-control blog-box text-white fw-bolder','placeholder':'Enter your Title'}),'desc':forms.Textarea(attrs={'class':'form-control blog-box fw-bolder text-white','placeholder':'Write something...','id':'message-text','row':3})}


class BlogPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactForm
        fields=['firstname','lastname','emailaddress','message']
        widgets={'firstname':forms.TextInput(attrs={'class':'form-control'}),'lastname':forms.TextInput(attrs={'class':'form-control'}),'emailaddress':forms.EmailInput(attrs={'class':'form-control'}),'firstname':forms.TextInput(attrs={'class':'form-control'}),}


    
