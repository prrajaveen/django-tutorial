from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required
def profile(request):
    return render(request,'myapplication/home.html')

@staff_member_required
def about(request):
    return render(request,'myapplication/about.html')