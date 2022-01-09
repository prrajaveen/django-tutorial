from django.shortcuts import render

# Create your views here.
def secondapplication(request):
    return render(request,'mysecondapplication/home.html')