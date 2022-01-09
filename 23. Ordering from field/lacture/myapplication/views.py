from django.shortcuts import render
from myapplication.models import Student
from myapplication.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    # fm=StudentRegistration(auto_id='%s')
    # if you want to add the filed name as a id name then use this
    fm=StudentRegistration(auto_id=True,label_suffix='  === ',initial={'name':'sonam','email':'sonam@gamil.com'})
    fm.order_fields(field_order=['first_name','name','email'])
    # if you set false it will remove label tag
    # fm=StudentRegistration(auto_id=False)
    return render(request,'myapplication/studetails.html',{'form':fm})