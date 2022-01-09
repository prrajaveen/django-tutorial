from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    course=models.CharField(max_length=70)  

    # def get_absolute_url(self):
    #     return reverse('thankyou') ####name of the url######

    ############ If you want to display signup data  ###########
    # def get_absolute_url(self):
    #     return reverse('detail',kwargs={'pk':self.pk})
