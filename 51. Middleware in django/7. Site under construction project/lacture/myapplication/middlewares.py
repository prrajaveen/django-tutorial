from django.shortcuts import HttpResponse,render

class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('call from middle ware')
        response=render(request,'myapplication/siteuc.html')
        return response