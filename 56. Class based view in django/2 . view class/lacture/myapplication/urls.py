from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('news/',views.NewsClassView.as_view(),name='news')
]