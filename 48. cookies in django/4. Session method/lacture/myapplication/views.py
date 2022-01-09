from django.http import response
from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.


# <=============== Set Session ====================>
def setsession(request):
    request.session['name']='sonam'
    request.session['lname']='jha'
    request.session.set_expiry(5)
    # if you want to expire on closing the browser then set 0
    # request.session.set_expiry(0)
    return render(request,'myapplication/setsession.html')


# <============= Get Session ====================>
def getsession(request):
    # name=request.session['name']
    # name=request.session.get('name',default='Guest')
    name=request.session.get('name')
    lname=request.session.get('lname')
    keys=request.session.keys()
    items=request.session.items()

    print("<","="*24,'>')
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    print('<','='*24,'>')
    # age=request.session.setdefault('age','26')


    return render(request,'myapplication/getsession.html',{'name':name,'lname':lname,'keys':keys,'items':items})



# <================== Delete Session ==============>
def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    # request.session.clear()
    return render(request,'myapplication/delsession.html')