from django.urls import path
from django.views.generic.base import RedirectView, TemplateView
from myapplication import views

urlpatterns=[
    path('',views.TemplateView.as_view(template_name='myapplication/home.html'),name='home'),
    path('home/',views.RedirectView.as_view(url='/something/'),name='home'),
    path('kumar/',views.RedirectView.as_view(pattern_name='home')),
    path('index/',views.RedirectView.as_view(url='/'),name='index'), 
    path('raja/',views.RajaRedirectView.as_view(),name='raja'),
    ##############  important #################################################
    path('praveen/<int:pk>/',views.PraveenRedirectView.as_view(),name='praveen'),
    path('<int:pk>/',views.TemplateView.as_view(template_name='myapplication/home.html'),name='root'),
    # path('praveen/<slug:post>/',views.PraveenRedirectView.as_view(),name='praveen'),
    # path('<slug:post>/',views.TemplateView.as_view(template_name='myapplication/home.html'),name='root')
]