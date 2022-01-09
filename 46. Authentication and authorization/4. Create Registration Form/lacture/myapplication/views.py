from django.shortcuts import render
from myapplication.forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def sign_up(request):
    
    if request.method=='POST':
        fm=RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'<h1>Your account has been secussfully created !!!</h1>')
    else:
        fm=RegistrationForm()
    return render(request,'myapplication/signup.html',{'form':fm})
