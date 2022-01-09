from django.shortcuts import render
from myapplication.forms import StudentRegistration

# Create your views here.
def ragistration(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            # print('name :',name)
    else:
        fm=StudentRegistration()
    return render(request,'myapplication/registration.html',{'form':fm})