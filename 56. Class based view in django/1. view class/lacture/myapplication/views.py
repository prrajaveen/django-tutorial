from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home page</h1>')

class MyView(View):
    name='praveen kuamr'
    def get(self,request):
        return HttpResponse(self.name)

class ChildClass(MyView):
    def get(self,request):
        return HttpResponse(self.name)