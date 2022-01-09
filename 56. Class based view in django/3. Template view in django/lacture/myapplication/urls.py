from django.urls import path
from myapplication import views

urlpatterns=[
    # path('',views.TemplateView.as_view(template_name='myapplication/home.html'),name='home'),
    # path('about/',views.TemplateView.as_view(template_name='myapplication/about.html'),name='about'),
    path('home/<int:roll>',views.Home.as_view(extra_context={'course':'python'}),name='home'),
    
]