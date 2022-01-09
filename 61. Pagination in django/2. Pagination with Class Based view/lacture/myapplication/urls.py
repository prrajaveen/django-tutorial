from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('detail/<int:pk>',views.PostDetailView.as_view(),name='detail')
]