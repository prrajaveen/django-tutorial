from django.shortcuts import render
from django.contrib.auth.models import User
from myapplication.models import Page,Post,Song

# Create your views here.
def show_home(request):
    data1=Page.objects.all()
    data2=Post.objects.all()
    data3=Song.objects.all()
    context={'data1':data1,'data2':data2,'data3':data3}
    return render(request,'myapplication/home.html',context)

def show_page(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(page_cat='programming')
    data3=Page.objects.filter(user__email='sonam@gmail.com')
    context={'data1':data1,'data2':data2,'data3':data3}
    return render(request,'myapplication/page.html',context)

def show_post(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(user__username='sonam')
    data3=Post.objects.filter(post_publish_date='2021-09-06')
    context={'data1':data1,'data2':data2,'data3':data3}
    return render(request,'myapplication/post.html',context)

def show_song(request):
    data1=Song.objects.all()
    data2=Song.objects.filter(user__username='rahul')
    data3=Song.objects.filter(song_duration=5)
    context={'data1':data1,'data2':data2,'data3':data3}
    return render(request,'myapplication/song.html',context)

def show_user(request):
    data1=User.objects.all()
    data2 = User.objects.filter(email='sonam@gmail.com')
    data3=User.objects.filter(page__page_cat='programming')
    data4=User.objects.filter(raja__post_publish_date='2021-09-05')
    data5=User.objects.filter(song__song_duration=5)
    context={'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5}
    return render(request,'myapplication/user.html',context)
