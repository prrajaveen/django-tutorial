from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.cache import cache



# Create your views here.

# Go to the middlewere in setting.py

def home(request):
    mv=cache.get('movie','has_expired')
    if mv == 'has_expired':
        cache.set('movie','raja',30)
        mv=cache.get('movie')
    return render(request,'myapplication/course.html',{'fm':mv})


def get_or_set(request):
    mv=cache.get_or_set('fees',5000,30,version=2)
    return render(request,'myapplication/fees.html',{'fm':mv})


def set_many(request):
    data={'name':'Sonam','roll':104}
    cache.set_many(data,30)
    mv=cache.get_many(data)
    return render(request,'myapplication/setmany.html',{'fm':mv})


def deletecache(request):
# <======= Signle object =============>
    # cache.delete('movie')
    cache.delete('fees',version=2)
    return HttpResponse('deleted ....')

def decrement_increment(request):
    # cache.set('roll',101,6000)
    # dv=cache.decr('roll',delta=2)
    incre=cache.incr('roll',delta=2)
    
    rv=cache.get('roll')
    return render(request,'myapplication/course.html',{'fm':rv})



def cache_clear(request):
    cache.clear()
    return HttpResponse('<h1>All cache clear ....</h1>')


