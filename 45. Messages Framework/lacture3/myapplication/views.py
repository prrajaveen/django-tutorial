from django.shortcuts import render
from myapplication.forms import StudentRegistration
from myapplication.models import User
from django.contrib import messages



# first See setting.py



# Create your views here.
def ragistration(request):
    messages.info(request,'Now you can login')
    messages.success(request,'Update ho gaya hai')
    messages.warning(request,'This is warning')
    messages.error(request,'This is an error')
    fm=StudentRegistration()
    return render(request,'myapplication/registration.html',{'form':fm})
