from django.http import response
from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def setcookie(request):
    response=render(request,'myapplication/setcookie.html')
    #<=======it will set 60 sec cookies and then expire============>
    # response.set_cookie('name','praveen',max_age=60)
    # <========== if you want to set in days ================>
    response.set_signed_cookie('name','praveen',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie('lname','kumar')
    return response

def getcookie(request):
   
    name=request.get_signed_cookie('name',salt='nm', default='Guest')
    return render(request,'myapplication/getcookie.html',{'name':name})
    

def delcookie(request):
    response=render(request,'myapplication/delcookie.html')
    response.delete_cookie('name')
    response.delete_cookie('lname')
    return response

    # 52 minute

