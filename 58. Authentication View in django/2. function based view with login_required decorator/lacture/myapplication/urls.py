from django.urls import path
from myapplication import views

urlpatterns=[
    path('accounts/profile/',views.profile,name='home'),
    path('about/',views.about,name='about')
]