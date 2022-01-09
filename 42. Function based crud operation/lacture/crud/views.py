from django import http
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from crud.forms import StudentForm
from crud.models import Student

# Create your views here.
def home(request):
    studentinfo=Student.objects.all()
    fm=StudentForm()
    return render(request,'crud/home.html',{'form':fm,'student':studentinfo})

def registration(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Your are not able to register')
        
def update(request,id):
    studentinfo=Student.objects.all()
    onestudent=Student.objects.get(pk=id)
    if request.method=='POST':
        fm=StudentForm(request.POST,instance=onestudent)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm=StudentForm(instance=Student.objects.get(pk=id))
    return render(request,'crud/update.html',{'form':fm,'student':studentinfo})

def delete(request,id):
    if request.method=='POST':
        stu=Student.objects.get(pk=id)
        stu.delete()
        return HttpResponseRedirect('/')
