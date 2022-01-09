from django.urls import path
from myapplication import views

urlpatterns=[
    path('studetail/<int:pk>/',views.StudentDetailView.as_view(),name='studetail'),
    path('stulist/',views.StudentListView.as_view(),name='stulist')

]