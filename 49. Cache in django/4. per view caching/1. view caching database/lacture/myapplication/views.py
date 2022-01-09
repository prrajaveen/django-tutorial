from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.

# Go to the middlewere in setting.py
@cache_page(30)
def home(request):
    return render(request,'myapplication/course.html')

def contact(request):
    return render(request,'myapplication/contact.html')