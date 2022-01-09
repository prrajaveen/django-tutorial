from django.shortcuts import render

# Create your views here.




def show_details(request,year):
    data={'yr':year}
    return render(request,'myapplication/show.html',data)




