from django.shortcuts import render
from myapplication.models import Student
from myapplication.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    stud=Student.objects.all()
    fm=StudentRegistration()
    return render(request,'myapplication/studetails.html',{'stu':stud,'form':fm})