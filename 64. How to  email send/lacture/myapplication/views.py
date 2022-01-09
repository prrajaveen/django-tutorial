
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from myapplication.forms import SendEmailform,OtpForm
from django.views import View
from django.core.mail import send_mail
from django.http import HttpResponse, request
import random


# Create your views here.


class Home(View):
    def get(self, request):
        return render(request,'myapplication/home.html')

    def post():
        fm=SendEmailform(request.POST)
        otp=random.randint(1111,9999)
        if fm.is_valid():

            
        