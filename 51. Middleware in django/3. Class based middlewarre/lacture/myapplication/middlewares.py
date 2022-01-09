#<============function based middleware====================>
# def my_middleware(get_response):
#     print("one time initialization")
#     def my_function(request):
#         # this code will run before view function call
#         print("this is before view")
#         response=get_response(request)
#         #this code will run after view function
#         print('This is after view')
#         return response
#     return my_function



# <================= Class based Middleware=============>
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('One time initialization')
    
    def __call__(self,request):
        # it will run befor view function run
        print("This code run before view function")
        response = self.get_response(request)
        print('this code execute after view')
        return response