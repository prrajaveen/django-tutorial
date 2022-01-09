from django.db import models
from django.forms.widgets import EmailInput

# Create your models here.

class Blogpost(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()

class ContactForm(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    emailaddress=models.CharField(max_length=100)
    message=models.TextField(max_length=100)