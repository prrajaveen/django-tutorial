from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapplication/home.html')

def about(request):
    return render(request,'myapplication/about.html')