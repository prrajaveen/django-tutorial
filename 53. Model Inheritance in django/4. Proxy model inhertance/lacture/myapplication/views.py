from django.shortcuts import render
from myapplication.models import ExamCenter,MyExamCenter

# Create your views here.
def home(request):
    examcenter=ExamCenter.objects.all()
    myexamcenter=MyExamCenter.objects.all()
    context={'examcenter':examcenter,'myexamcenter':myexamcenter}
    return render(request,'myapplication/home.html',context)
