from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.Home.as_view(),name='home')
]