from django.shortcuts import render
from .models import Student,ProxyStudent

# Create your views here.
def home(request):
    students=Student.objects.all()
    # proxystudents=ProxyStudent.students.roll_range(101,105)
    proxystudents=ProxyStudent.students.rollgraterthan(101)

    return render(request,'myapplication/home.html',{'students':students,'proxystudents':proxystudents})