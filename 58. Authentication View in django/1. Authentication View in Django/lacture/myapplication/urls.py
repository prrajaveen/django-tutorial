from django.urls import path
from django.urls.conf import include
from myapplication import views

urlpatterns=[
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/profile/',views.Profile.as_view(),name='profile')
]