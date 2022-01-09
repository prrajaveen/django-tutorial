from django.urls import path
from myapplication import views

urlpatterns=[
    path('create/',views.StudentCreateView.as_view(),name='home'),
    path('thankyou/',views.StudentThankTemplateView.as_view(),name='thankyou'),
    path('update/<int:pk>',views.StudentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.StudentDeteteView.as_view(),name='delete'),
]