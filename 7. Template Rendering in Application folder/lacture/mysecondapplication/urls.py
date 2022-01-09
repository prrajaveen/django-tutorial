from django.urls import path
from mysecondapplication import views

urlpatterns=[
    path('',views.secondapplication)
]