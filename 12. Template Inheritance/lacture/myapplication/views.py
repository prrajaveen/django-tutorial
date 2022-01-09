from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myapplication/index.html',{'color':'white'})
def about(request):
    return render(request,'myapplication/about.html',{'color':'aboutwhite'})
def contact(request):
    return render(request,'myapplication/contact.html',{'color':'pink'})