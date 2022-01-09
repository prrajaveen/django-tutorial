from django.shortcuts import render
from django.http import HttpResponse
from myapplication import signals

# Create your views here.
def home(request):
    signals.notification.send(sender=None,request=request,user=['praveen','kumar'])
    return HttpResponse('Home page')