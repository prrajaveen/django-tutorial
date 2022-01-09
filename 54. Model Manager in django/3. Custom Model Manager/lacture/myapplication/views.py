from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    students=Student.objects.all()
    return render(request,'myapplication/home.html',{'students':students})