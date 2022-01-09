from django.urls import path
from thirdapplication import views

urlpatterns=[
    path('',views.thirdapp)
]