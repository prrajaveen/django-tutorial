from typing import Union
from django.shortcuts import render
from myapplication.models import Student
from django.db.models import Q


# Create your views here.



def home(request):
    # student_data=Student.objects.filter(Q(id=6) & Q(roll=107))
    # student_data=Student.objects.filter(Q(id=6) | Q(roll=107))
    student_data=Student.objects.filter(~Q(id=6))
   

    print('Return :',student_data)
    print('\n')
    print("SQL Query :",student_data.query)
    return render(request,'myapplication/home.html',{'students':student_data})

