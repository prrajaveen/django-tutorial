from django.contrib.auth import authenticate, update_session_auth_hash
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from myapplication.forms import RegistrationForm,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm

from django.contrib.auth import login,logout,authenticate
# Create your views here.



# <================ Sign up Page ==================>
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
                    
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'myapplication/login.html',{'form':fm})

    else:
        return HttpResponseRedirect('/profile/')


# <============ Profile page =================>
def user_profile(request):

    # if user autheticathed then render profile.html
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your profile has been updated')
        else:
            fm=EditUserProfileForm(instance=request.user)
        return render(request,'myapplication/profile.html',{'name':request.user,'form':fm})
    else:
        #if user not authenticated the redirect to login page
        return HttpResponseRedirect('/login/')



# <================== Logout =======================>
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



# <=================== Change password with old Password ===============>
def user_change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password had been secussfully changed !!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'myapplication/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')



# <==================== Change Password withou Old Password ==================>
def user_change_password_without_old_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password had been secussfully changed !!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'myapplication/withoutoldpassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')