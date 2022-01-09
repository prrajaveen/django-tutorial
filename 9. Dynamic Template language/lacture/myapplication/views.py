from django.shortcuts import render

# Create your views here.
def index(request):
    params={'intro':'my name is praveen kumar . I am from muzaffarpur bihar. I have completed my 12th from Bihar school Examination Board. after I have doen my graduation from Rajiv gandhi Technical universty. i become to seccussful in my life is my life inpiration. i am honest and dadicated to work is my strength. always find easy way to do any work is my weakness'}
    newparms={'url':'https//:google.com'}
    return render(request,'myapplication/index.html',{'myintro':params,'url':newparms,'value':False})