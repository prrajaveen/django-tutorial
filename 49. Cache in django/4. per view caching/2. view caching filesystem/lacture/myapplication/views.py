from django.shortcuts import render



# <==========if you want to use cache_page in url=============>


# Create your views here.

# Go to the middlewere in setting.py
# @cache_page(30)
# def home(request):
#     return render(request,'myapplication/course.html')

def home(request):
    return render(request,'myapplication/course.html')

def contact(request):
    return render(request,'myapplication/contact.html')