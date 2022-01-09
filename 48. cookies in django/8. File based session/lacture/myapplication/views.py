from django.http import response
from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse

# Create your views here.


# <=============== Set Session ====================>
def setsession(request):
    request.session['name']='sonam'
    return render(request,'myapplication/setsession.html')


# <============= Get Session ====================>
def getsession(request):
    name=request.session.get('name')
    return render(request,'myapplication/getsession.html',{'name':name})




# <================== Delete Session ==============>
def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    # request.session.clear()
    return render(request,'myapplication/delsession.html')