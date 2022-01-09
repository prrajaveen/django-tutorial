from typing import SupportsAbs
from django.shortcuts import render
from myapplication.models import ExamCenter,Student

# Create your views here.
def home(request):
    students=Student.objects.all()
    examcenters=ExamCenter.objects.all()
    context={'students':students,'centers':examcenters}
    return render(request,'myapplication/home.html',context)