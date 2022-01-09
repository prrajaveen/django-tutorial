from myapplication import views
from django.urls import path
from django.views.decorators.cache import cache_page


urlpatterns=[
    path('',cache_page(60)(views.home)),
    path('home/',views.home),
    path('contact/',views.contact)
]