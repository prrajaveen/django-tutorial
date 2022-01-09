from typing import Union
from django.shortcuts import render
from myapplication.models import Student
from django.db.models import Q
from datetime import date,time
from django.db.models import Avg,Sum,Min,Max,Count

# Create your views here.



def home(request):
    
    student_data=Student.objects.all()
    average=student_data.aggregate(Avg('marks'))
    total_marks=student_data.aggregate(Sum('marks'))
    minimum_marks=student_data.aggregate(Min('marks'))
    maximum_marks=student_data.aggregate(Max('marks'))
    total_count=student_data.aggregate(Count('marks'))


    context={'students':student_data,'average':average,'total_marks':total_marks,'minimum_marks':minimum_marks,'maximum_marks':maximum_marks,'total_count':total_count}
    print('Return :',student_data)
    print('\n')
    print("SQL Query :",student_data.query)
    return render(request,'myapplication/home.html',context)

