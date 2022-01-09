from django.urls import path
from django.urls.resolvers import URLPattern
from secondapplication import views

urlpatterns=[
    path('',views.secondapp)
]