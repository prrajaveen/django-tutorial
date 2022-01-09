from django.shortcuts import render
from django.http import HttpResponse

#======================== Guideline ===============================>
#   first install the application to setting
#   second include the app url to the project url
#   third create your views
#   forth define the url for your views to your application urls
#<==================================================================>

# Create your views here.
def learn_django(request):
    return HttpResponse('hello django')

def learn_python(request):
    return HttpResponse('<h1>hello python</h1>')

def learn_var(request):
    a='<h1>hello variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a=10+10
    return HttpResponse(a)

def learn_format(request):
    a='praveen'
    return HttpResponse(f'Hello How are you {a}')