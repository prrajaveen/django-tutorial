from django.forms.fields import EmailField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from myapplication.models import Student
from myapplication.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print('Name :',name)
            print('Email :',email)
            print('password',password)
            return HttpResponseRedirect('/success')
            # return render(request,'myapplication/success.html',{'nm':name})
    fm=StudentRegistration()

    return render(request,'myapplication/studetails.html',{'form':fm})

def thankyou(request):
    return render(request,'myapplication/success.html')