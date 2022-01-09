from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapplication/home.html',{'color':'red'})

def contact(request):
    return render(request,'myapplication/contact.html',{'color':'green'})

def about(request):
    return render(request,'myapplication/about.html',{'color':'yellow'})

def blog(request):
    return render(request,'myapplication/blog.html',{'color':'purple'})
