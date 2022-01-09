from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.show_home,name='home'),
    path('page/',views.show_page,name='page'),
    path('post/',views.show_post,name='post'),
    path('song/',views.show_song,name='song'),
    path('user/',views.show_user,name='user'),
]