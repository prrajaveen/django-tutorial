from django.shortcuts import render
from myapplication.models import Student, Teacher ,Contractor
# Create your views here.
def home(request):
    students=Student.objects.all()
    teachers=Teacher.objects.all()
    contractors=Contractor.objects.all()
    print(teachers)
    context={'teachers':teachers,'students':students,'contracors':contractors}
    return render(request,'myapplication/home.html',context)