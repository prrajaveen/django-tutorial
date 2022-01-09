from django.shortcuts import render

# Create your views here.




def show_details(request,my_id,id):
    print(my_id)
    
    data={'my_id':my_id,'id':id}
    return render(request,'myapplication/show.html',data)

def homepage(request,check):
    return render(request,'myapplication/home.html',{'check':check})



