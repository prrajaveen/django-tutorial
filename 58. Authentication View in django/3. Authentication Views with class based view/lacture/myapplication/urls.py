from django.urls import path
from myapplication import views


urlpatterns=[
    path('accounts/profile/',views.Profile.as_view(),name='home'),
]