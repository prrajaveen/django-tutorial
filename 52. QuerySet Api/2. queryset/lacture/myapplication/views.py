from typing import Union
from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.


# <========================= Return all object =============================>
def home(request):
# <============ It will return all the data in object form =================>
    # student_data=Student.objects.all()
# <------------------------------------------------------------------------->

# <=========== It will return who marks is 80 and city is ranchi============>
    # student_data=Student.objects.filter(marks=80)
    # student_data=Student.objects.filter(city='ranchi')
#<--------------------------------------------------------------------------->

# <============ it will return whose marks is not 80 ========================>
    # student_data=Student.objects.exclude(marks=80)
# <-------------------------------------------------------------------------->

# <============= it will return in Accending order ==========================>
    # student_data=Student.objects.order_by('city')
    # student_data=Student.objects.order_by('marks')
# <-------------------------------------------------------------------------->

# <====================== capital/small lattter problem======================>
    # capital latter show first
# <-------------------------------------------------------------------------->

# <================ it will return in decencing order =======================>
    # student_data=Student.objects.order_by('-marks')
# <-------------------------------------------------------------------------->

# <========================= It will pick in Random =========================>
    # student_data=Student.objects.order_by('?')
# <-------------------------------------------------------------------------->

# <=============== it will return in Reverse order ==========================>
    # student_data=Student.objects.order_by('id').reverse()
# <-------------------------------------------------------------------------->
    
# <================ it will return first five table data =====================>
    # student_data=Student.objects.order_by('id')[:5]
# <---------------------------------------------------------------------------> 

# <================ It will return Last Five table data ======================>
    # student_data=Student.objects.order_by('id').reverse()[:5]
# <--------------------------------------------------------------------------->


# <========== it will return all the date list inside dictionary =============>
    # student_data=Student.objects.values()
# <--------------------------------------------------------------------------->

# <=========== it will show two column with list inside dictionary============>
    # student_data=Student.objects.values('name','city')
# <--------------------------------------------------------------------------->

# <===================== it will return list tupple ==========================>
    # student_data=Student.objects.values_list('city')
    # student_data=Student.objects.values_list('id','name',named=True)
# <--------------------------------------------------------------------------->

# <================== it will return all data using database name==============>
    # student_data=Student.objects.using('default')
# <---------------------------------------------------------------------------->

# <========= return how many data in day,month year ===========================>
    # student_data=Student.objects.dates('pass_date','day')

############################# Second Table Teacher #############################

# <=================== union (both data with no duplicate) ====================>
    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs1.union(qs1) #### No duplicate #####
    # student_data=union(qs2,qs1)
    # student_data=qs2.union(qs1, all=True) #### Duplicate True #####
#<--------------------------------------------------------------------------->

# <=========== Intersection (common data show) ==============================>
    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs1.intersection(qs2)
# <-------------------------------------------------------------------------->

# <============  Differance (common data exclude) ===========================>
    
    # qs1=Student.objects.values_list('id','name',named=True)
    # qs2=Teacher.objects.values_list('id','name',named=True)
    # student_data=qs1.difference(qs2) # student-teacher = remainder student
    # student_data=qs2.difference(qs1) #Teacher-student   =  reaminder teacher
# <-------------------------------------------------------------------------->


#################### (&and operator) and (|or operator) #######################
# <=============================== And Operator ================================>
    # student_data=Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data=Student.objects.filter(id=6,roll=6)
    # student_data=Student.objects.filter(Q(id=5) & Q(roll=107))
# <----------------------------------------------------------------------------->

# <=============================== Or Operator ================================>
    # student_data=Student.objects.filter(id=7) | Student.objects.filter(roll=106)
    student_data=Student.objects.filter(Q(id=7) | Q(roll=106))
# <----------------------------------------------------------------------------->


    
    
    
    print('return:',student_data)
    print("\n\n")
    print("sql Query",student_data.query)
    return render(request,'myapplication/home.html',{'students':student_data})

