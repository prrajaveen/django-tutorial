from django.urls import path
from myapplication import views

urlpatterns=[
    path('signup/',views.sign_up,name='signup'),
]