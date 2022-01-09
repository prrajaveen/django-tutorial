from django.shortcuts import render
from django.http import HttpResponse

#======================== Guideline ===============================>
#   first install the application to setting
#   second include the app url to the project url
#   third create your views
#   forth define the url for your views to your application urls
#<==================================================================>

# Create your views here.
def index(request):
    return render(request,'index.html')

