from django.http.response import HttpResponseRedirect
from matplotlib import pyplot as plt

from django.shortcuts import render
from myapplication.forms import BlogSignupForm,BlogLoginForm,BlogPostForm,BlogPasswordChangeForm,ContactForm
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from myapplication.models import Blogpost

# Create your views here.

# <==================== Home page ==================>
def home(request):
    return render(request,'myapplication/home.html',{'homecolor':'text-warning rounded active'})

# <==================== Abhout page ==================>
def about(request):
    return render(request,'myapplication/about.html',{'aboutcolor':'text-warning rounded'})

# <==================== Contact page ==================>
def contact(request):
    if request.method=='POST':
        fm=ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your Feedback has been sussesfully sent')
            return HttpResponseRedirect('/contact/')
    else:
        fm=ContactForm()
    return render(request,'myapplication/contact.html',{'contactcolor':'text-warning rounded','form':fm})

# <==================== Dashboard ==================>
def dashboard(request):
    if request.user.is_authenticated:
        blogpost=Blogpost.objects.all()
        fm=BlogPostForm()
        return render(request,'myapplication/dashboard.html',{'form':fm,'post':blogpost,'dashboardcolor':'text-warning'})
    else:
        return HttpResponseRedirect('/login/')

# <==================== Login page ==================>
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=BlogLoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upassword=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upassword)
                if user is not None:
                    login(request,user)
                    messages.success(request,'You have secussfully logged in')
                    return HttpResponseRedirect('/dashboard/')    
        else:
            fm=BlogLoginForm()       
        return render(request,'myapplication/login.html',{'form':fm,'logincolor':'text-warning'})
    else:
        return HttpResponseRedirect('/dashboard/')


# <==================== Signup page ==================>
def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=BlogSignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your Account has been secussfully created')         
        else:
            fm=BlogSignupForm()
        return render(request,'myapplication/signup.html',{'form':fm,'signupcolor':'text-warning'})
    else:
        return HttpResponseRedirect('/dashboard/')

# <==================== Logout view ==================>
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    pass


# <====================== New Blog post ======================>
def blog_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=BlogPostForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Added new Blog Post')
                return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


# <================== Update Blog post ================>

def update_post(request,id):
    bloginstance=Blogpost.objects.get(pk=id)
    if request.method=='POST':
        fm=BlogPostForm(request.POST,instance=bloginstance)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your post has been secussfuly updated')
            return HttpResponseRedirect('/dashboard/')


#<====================== Delete Post =======================>

def Delete_post(request,id):
    if request.method=='POST':
        bloginstance=Blogpost.objects.get(pk=id)
        bloginstance.delete()
        messages.success(request,'Your Post has been seccessfully deleted')
        return HttpResponseRedirect('/dashboard/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=BlogPasswordChangeForm(user=request.user,data=request.POST)
            print('hello')
            if fm.is_valid():
                fm.save()
                messages.success(request,"Your Password has been secussfully changed")
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/dashboard/')
        else:
            fm=BlogPasswordChangeForm(user=request.user)
        print(request.user.id)
        return render(request,'myapplication/passwordchange.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
