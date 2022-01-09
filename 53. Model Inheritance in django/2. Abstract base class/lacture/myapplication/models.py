from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class commoninfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract = True


class Student(commoninfo):
    fees=models.IntegerField()
    date=None
    
class Teacher(commoninfo):
    salary=models.IntegerField()

class Contractor(commoninfo):
    date=models.DateTimeField()
    payment=models.IntegerField()
    