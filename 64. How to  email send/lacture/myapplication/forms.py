from django import forms
from django.forms import widgets
class SendEmailform(forms.Form):
    subject=forms.CharField(widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput())
    message=forms.CharField(widget=forms.TextInput())

class OtpForm(forms.Form):
    otp=forms.ImageField(widget=forms.IntegerField())
    