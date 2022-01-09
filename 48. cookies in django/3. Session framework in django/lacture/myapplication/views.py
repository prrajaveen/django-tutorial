from django.http import response
from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def setsession(request):
    request.session['name']='sonam'
    request.session['lname']='jha'
    return render(request,'myapplication/setsession.html')

def getsession(request):
    # name=request.session['name']
    # name=request.session.get('name',default='Guest')
    name=request.session.get('name')
    lname=request.session.get('lname')

    return render(request,'myapplication/getsession.html',{'name':name,'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'myapplication/delsession.html')