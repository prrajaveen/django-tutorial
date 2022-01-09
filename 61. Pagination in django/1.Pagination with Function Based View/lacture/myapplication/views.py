from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    all_post=Post.objects.all().order_by('id')
    paginator=Paginator(all_post,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    print(paginator)
    print(page_number)
    print(page_obj)
    return render(request,'myapplication/home.html',{'posts':page_obj})