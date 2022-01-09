from django.shortcuts import render
from myapplication.models import Student
from myapplication.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    fm=StudentRegistration(initial={'name':'Rahul'})
    return render(request,'myapplication/studetails.html',{'form':fm})