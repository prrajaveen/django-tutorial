from django.shortcuts import render
from myapplication.models import Student
from myapplication.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Name :',fm.cleaned_data['name'])
            print('Email :',fm.cleaned_data['email'])
    fm=StudentRegistration()

    return render(request,'myapplication/studetails.html',{'form':fm})