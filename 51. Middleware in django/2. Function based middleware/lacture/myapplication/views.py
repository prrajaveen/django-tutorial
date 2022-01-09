from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    print("i am view")
    return HttpResponse("This is home page")