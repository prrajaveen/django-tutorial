from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('info/',views.StudentInfo.as_view(),name='info'),
    path('stuinfo',views.StudentUsingCustomTemplateName.as_view(),name='stuinfo')
]