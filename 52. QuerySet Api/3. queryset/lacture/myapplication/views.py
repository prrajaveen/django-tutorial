from typing import Union
from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.


def home(request):
# <======================= It retrive specific data ========================>
    # student_data=Student.objects.get(pk=1)
# <------------------------------------------------------------------------->

# <======================= It return first data ========================>
    # student_data=Student.objects.first() # It will return first data
    # student_data=Student.objects.order_by('name').first() #first it will order then return first data
    # student_data=Student.objects.last()   # it will return last data from table
    # student_data=Student.objects.latest('pass_date')  # It will return data form by pass_date
    # student_data=Student.objects.earliest('pass_date')    # It will show oldest data of pass_date    
# <------------------------------------------------------------------------->

# <======== if data exits then return True otherwise False =================>
    # student_data=Student.objects.all()
    # print(student_data.exists())  
    #------------------------------
    # one_data=Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.id).exists())
# <------------------------------------------------------------------------->

# <=========================== save() method ==================================>
    # student_data=Student(name='Sameer',roll=112,city='muz',marks=40,pass_date='2020-05-4')
    # student_data.save()
# <-------------------------------------------------------------------------->

# <========================= create() method =================================>
    # student_data=Student.objects.create(name='rohan das',roll=113,city='patna',marks=40,pass_date='2020-06-4')
# <-------------------------------------------------------------------------->

# <========================= create_or_get() method =================================>
    # student_data,created =Student.objects.get_or_create(name='rohan das',roll=115,city='patna',marks=40,pass_date='2020-06-4')
    # print(created) # if data abaliable the created False then created False
# <-------------------------------------------------------------------------->

# <========================== update() method ================================>
    # Student.objects.filter(id=10).update(name='Anant',marks=101)
    # Student.objects.filter(marks=40).update(city='pass')
    # student_data=Student.objects.get(id=10)
# <--------------------------------------------------------------------------->


# <========================== update_or_create() method ================================>
    # student_data,created=Student.objects.update_or_create(id=14,name='rohan das',defaults={'name':'sameer'})
    # print(created)
# <------------------------------------------------------------------------------------->


# <========================== bulk_create() method ================================>
# not work with many to may relationship
    # objs=[
    #     Student(name='Asif',roll=116,city='Dhanbad',marks=70,pass_date='2020-5-4'),
    #     Student(name='gilli',roll=117,city='Hadrabad',marks=80,pass_date='2020-5-5'),
    #     Student(name='harry',roll=118,city='Bengluru',marks=90,pass_date='2020-5-6'),
    # ]
    # student_data = Student.objects.bulk_create(objs)
# <------------------------------------------------------------------------------------->

# <========================== bulk_update() method ================================>
# not work with many to may relationship
#you cannot update primary key
#it will not send pre_save and post_save signal
#if objs contain duplicate, only the first one is updated
    # all_student_data=Student.objects.all()
    # for stu in all_student_data:
    #     stu.city='Bhel'
    # student_data=Student.objects.bulk_update(all_student_data,['city'])
# <------------------------------------------------------------------------------------->

# <========================== in_bulk() method ================================>
    # student_data=Student.objects.in_bulk()
    # student_data=Student.objects.in_bulk([1,2])
    # print(student_data)
# <------------------------------------------------------------------------------------->

# <============================== delete() method ==========================================>
    # student_data=Student.objects.get(pk=17).delete()
    # student_data=Student.objects.filter(marks=40).delete()
# <------------------------------------------------------------------------------------->

# <============================== count() method ==========================================>
    student_data=Student.objects.all()
    print(student_data.count())
# <------------------------------------------------------------------------------------->

# <============================= explain() mehtod ========================================>
    print(Student.objects.all().explain())

# <--------------------------------------------------------------------------------------->





    # print('return:',student_data)
    # print("\n\n")
    # print("sql Query",student_data.query)
    return render(request,'myapplication/home.html',{'students':student_data})

