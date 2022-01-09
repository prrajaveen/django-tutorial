from typing import Union
from django.shortcuts import render
from myapplication.models import Student
from django.db.models import Q
from datetime import date,time

# Create your views here.


# <========================= Return all object =============================>
def home(request):
    # student_data=Student.objects.all()
    # student_data=Student.objects.filter(name__exact='sonam')    #<------ case sensetive --------->
    # student_data=Student.objects.filter(name__iexact='Sonam')   #<------- No case sensative -------->
    # student_data=Student.objects.filter(name__contains='s')     # <----- it will return all data have s ---->
    # student_data=Student.objects.filter(name__icontains='A')    # <----- it will return all data have s ----> <-no case sensetive--->
    # student_data=Student.objects.filter(id__in=[1,5,7])         # <------ it will give 1 5 and row --------->
    # student_data=Student.objects.filter(marks__in=[50,70])      # <------ it will give 1 5 and row --------->
    # student_data=Student.objects.filter(marks__gt=50)
    # student_data=Student.objects.filter(marks__gte=50)
    # student_data=Student.objects.filter(marks__lt=50)
    # student_data=Student.objects.filter(marks__lte=50)
    # student_data=Student.objects.filter(name__startswith='s')
    # student_data=Student.objects.filter(name__istartswith='S')
    # student_data=Student.objects.filter(city__endswith='i')
    # student_data=Student.objects.filter(city__iendswith='I')
    # student_data=Student.objects.filter(pass_date__range=('2021-08-01','2021-08-08'))
    # student_data=Student.objects.filter(admdatetime__date=date(2021,7,5))
    # student_data=Student.objects.filter(admdatetime__date__gte=date(2021,7,5))
    # student_data=Student.objects.filter(pass_date__year__gte=2021)
    # student_data=Student.objects.filter(pass_date__month=11)
    # student_data=Student.objects.filter(pass_date__day__lte=10)
    # student_data=Student.objects.filter(pass_date__week=37)
    # student_data=Student.objects.filter(pass_date__week_day=1)
    # student_data=Student.objects.filter(pass_date__quarter=3)
    # student_data=Student.objects.filter(admdatetime__time__gt=time(6,00))
    # student_data=Student.objects.filter(admdatetime__hour__gt=8)
    # student_data=Student.objects.filter(admdatetime__minute__gt=26)
    # student_data=Student.objects.filter(admdatetime__second__gt=20)
    student_data=Student.objects.filter(roll__isnull=False)

    print('Return :',student_data)
    print('\n')
    print("SQL Query :",student_data.query)
    return render(request,'myapplication/home.html',{'students':student_data})

