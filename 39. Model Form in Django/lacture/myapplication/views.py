from django.shortcuts import render
from myapplication.forms import StudentRegistration
from myapplication.models import User

# Create your views here.
def ragistration(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=User(name=name,email=email,password=password)
            reg.save()
    else:
        fm=StudentRegistration()
    return render(request,'myapplication/registration.html',{'form':fm})
