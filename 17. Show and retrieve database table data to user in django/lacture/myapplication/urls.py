from django.urls import path
from myapplication import views
urlpatterns=[
    path('stu/',views.studentinfo)
]