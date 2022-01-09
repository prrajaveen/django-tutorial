from django.http import response
from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def setcookie(request):
    response=render(request,'myapplication/setcookie.html')
    #<=======it will set 60 sec cookies and then expire============>
    # response.set_cookie('name','praveen',max_age=60)
    # <========== if you want to set in days ================>
    response.set_cookie('name','praveen',expires=datetime.utcnow()+timedelta(days=2))
    response.set_cookie('lname','kumar')
    return response

def getcookie(request):
    # name=request.COOKIES['name']
    name=request.COOKIES.get('name','guest')
    return render(request,'myapplication/getcookie.html',{'name':name})
    

def delcookie(request):
    response=render(request,'myapplication/delcookie.html')
    response.delete_cookie('name')
    return response

    # 52 minute

