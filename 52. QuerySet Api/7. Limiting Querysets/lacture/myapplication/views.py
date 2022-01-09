from typing import Union
from django.shortcuts import render
from myapplication.models import Student
from django.db.models import Q


# Create your views here.



def home(request):
    # student_data=Student.objects.all()[5:]
    # student_data=Student.objects.all()[:5]
    student_data=Student.objects.all().reverse()[5:]
    # student_data=Student.objects.all()[:11:2]
   

    print('Return :',student_data)
    print('\n')
    print("SQL Query :",student_data.query)
    return render(request,'myapplication/home.html',{'students':student_data})

