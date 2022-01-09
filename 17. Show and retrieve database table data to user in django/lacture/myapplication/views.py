from django.shortcuts import render
from myapplication.models import Student
# Create your views here.

def studentinfo(request):
    stud=Student.objects.all()
    return render(request,'myapplication/studetails.html',{'stu':stud})