from django import http
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from crud.forms import StudentForm
from crud.models import Student
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.

        
# def update(request,id):
#     studentinfo=Student.objects.all()
#     onestudent=Student.objects.get(pk=id)
#     if request.method=='POST':
#         fm=StudentForm(request.POST,instance=onestudent)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')
#     else:
#         fm=StudentForm(instance=Student.objects.get(pk=id))
#     return render(request,'crud/update.html',{'form':fm,'student':studentinfo})



class Home(TemplateView):
    template_name='crud/home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentForm()
        stud=Student.objects.all()
        context={'form':fm,'student':stud}
        return context
    
    def post(self,request):
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

class StudentDelete(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        id=kwargs.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return super().get_redirect_url(*args,**kwargs)
    
class Studentupdate(View):
    def get(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)
        stu= Student.objects.all()
        return render(request,'crud/update.html',{'form':fm,'student':stu})
    def post(self,request,id):
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')





