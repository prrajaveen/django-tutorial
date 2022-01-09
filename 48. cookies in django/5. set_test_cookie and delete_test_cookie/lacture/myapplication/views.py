from django.http import response
from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.


# <=============== Set test cookie ====================>
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'myapplication/settestcookie.html')

# <============ Check Test cookie ===================>
def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request,'myapplication/checktestcookie.html')

# <============ Delete Test cookie ======================>
def deletetestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'myapplication/deletetestcookie.html')