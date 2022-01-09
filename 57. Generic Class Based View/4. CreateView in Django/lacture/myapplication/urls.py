from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.StudentFormView.as_view(),name='home'),
    path('thankyou/',views.ThankView.as_view(),name='thankyou'),
    path('detail/<int:pk>',views.StudentDetailView.as_view(),name='detail')
]