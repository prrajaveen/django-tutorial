from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    students=Student.students.roll_range(101,105)
    return render(request,'myapplication/home.html',{'students':students})