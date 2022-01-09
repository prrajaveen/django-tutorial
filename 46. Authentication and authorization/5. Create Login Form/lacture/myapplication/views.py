from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from myapplication.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def sign_up(request): 
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'<h1>Your account has been secussfully created !!!</h1>')
        else:
            fm=RegistrationForm()
        return render(request,'myapplication/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


# Login System
def login_form(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'myapplication/login.html',{'form':fm})

    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):

    # if user autheticathed then render profile.html
    if request.user.is_authenticated:
        return render(request,'myapplication/profile.html',{'name':request.user})
    else:
        #if user not authenticated the redirect to login page
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
