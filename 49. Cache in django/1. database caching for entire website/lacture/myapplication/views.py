from django.shortcuts import render

# Create your views here.

# Go to the middlewere in setting.py

def home(request):
    return render(request,'myapplication/course.html')