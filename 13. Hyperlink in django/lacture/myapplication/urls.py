from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('blog',views.blog,name='blog')
]