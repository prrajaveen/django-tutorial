from django.http import HttpResponse, response


class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_view(request,*args,**kwargs):
        print('This is process view before view')
        return None


class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        print('This is process exception middleware')
        msg=exception
        class_name=exception.__class__.__name__
        print(msg)
        print(class_name)
        return HttpResponse(class_name)
        # return None

class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_template_response(self,request,response):
        print("process template middleware from middleware")
        response.context_data['name']='sonam'
        return response