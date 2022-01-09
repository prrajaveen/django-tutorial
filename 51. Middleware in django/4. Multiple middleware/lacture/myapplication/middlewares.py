from django.http import HttpResponse

# <================= Class based Middleware=============>
class Brothermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time initialization')
    
    def __call__(self,request):
        # it will run befor view function run
        print("This Brother Middleware code run before view function")
        response = self.get_response(request)
        print('this Brother middleware code execute after view')
        return response

class Fathermiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time initialization')
    
    def __call__(self,request):
        # it will run befor view function run
        print("This is Father middleware code run before view function")
        # response = self.get_response(request)
        response=HttpResponse('nikal lo')
        print('this Father code execute after view')
        return response

class Mummymiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time initialization')
    
    def __call__(self,request):
        # it will run befor view function run
        print("This is Mummy middleware code run before view function")
        response = self.get_response(request)
        print('this Mummy code execute after view')
        return response