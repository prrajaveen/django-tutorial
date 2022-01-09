from django.shortcuts import render

# Create your views here.
def index(request):
    params={'name':'praveen kumar','roll':101,'city':'muzaffarpur'}
    return render(request,'myapplication/index.html',params)