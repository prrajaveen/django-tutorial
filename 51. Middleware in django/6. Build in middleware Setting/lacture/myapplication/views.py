from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print("i am view")
    return HttpResponse("This is home page")

def excp(request):
    a=1/0
    print("i am exception view")
    return HttpResponse('This is Exception view page')


def userinfo(request):
    print("i am user info view")
    context={'name':'praveen kumar'}
    
    return TemplateResponse(request,'myapplication/user.html',context)