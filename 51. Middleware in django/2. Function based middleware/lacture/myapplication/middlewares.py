
def my_middleware(get_response):
    print("one time initialization")
    def my_function(request):
        # this code will run before view function call
        print("this is before view")
        response=get_response(request)
        #this code will run after view function
        print('This is after view')
        return response
    return my_function