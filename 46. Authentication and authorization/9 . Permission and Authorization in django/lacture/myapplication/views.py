from django.contrib.auth import authenticate, update_session_auth_hash
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from myapplication.forms import RegistrationForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group, User
# Create your views here.



# <================ Sign up Page ==================>
def sign_up(request): 
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
                user=fm.save()
                group = Group.objects.get(name='editor')
                user.groups.add(group)
                messages.success(request,'<h1>Your account has been secussfully created !!!</h1>')
        else:
            fm=RegistrationForm()
        return render(request,'myapplication/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')


# <=============== Login System =====================>
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
                    messages.success(request,'Secussfully login !!!')
                    
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(request,'myapplication/login.html',{'form':fm})

    else:
        return HttpResponseRedirect('/dashboard/')


# <============ Dashboard page =================>
def user_dashboard(request):

    # if user autheticathed then render profile.html
    if request.user.is_authenticated:
        return render(request,'myapplication/dashboard.html',{'user':request.user})
        
    else:
        #if user not authenticated the redirect to login page
        return HttpResponseRedirect('/login/')



# <================== Logout =======================>
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



