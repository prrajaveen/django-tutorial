from django.shortcuts import render

# Create your views here.
def myfee(request):
    return render(request, 'fees.html')