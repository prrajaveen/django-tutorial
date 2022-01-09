from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)
    comment=models.CharField(max_length=70,default='not abliable')

    # def __str__(self):
    #     # return self.stuname
    #     # if return interger
    #     return str(self.stuid)

class Teacher(models.Model):
    tid=models.IntegerField()
    tname=models.CharField(max_length=70)
    temail=models.CharField(max_length=70)
    tpass=models.CharField(max_length=70)
    comments=models.CharField(max_length=10)