from django.db import models
from myapplication.managers import CustomManager

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    objects =  models.Manager()
   

class ProxyStudent(Student):
    students=CustomManager()
    class Meta:
        proxy=True
        ordering=['name']