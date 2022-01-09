from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.home,name='home'),
    path ('class/',views.MyView.as_view(name='raja'),name='class'),
    path('childclass/',views.ChildClass.as_view(),name='childclass')
]