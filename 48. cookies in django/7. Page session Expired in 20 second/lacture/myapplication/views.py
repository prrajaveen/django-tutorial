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
    if 'name' in request.session:
        name=request.session.get('name')
        request.session.modified=True
        return render(request,'myapplication/getsession.html',{'name':name})
    else:
        return HttpResponse('Your session has been expired')



# <================== Delete Session ==============>
def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    # request.session.clear()
    return render(request,'myapplication/delsession.html')