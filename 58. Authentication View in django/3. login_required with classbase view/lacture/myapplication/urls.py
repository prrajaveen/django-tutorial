from django.urls import path
from myapplication import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns=[
    path('accounts/profile/',views.Profile.as_view(),name='home'),
    # path('accounts/profile/',login_required(views.Profile.as_view()),name='home'),
    # path('accounts/profile/',staff_member_required(views.Profile.as_view()),name='home'),
    path('about/',views.About.as_view(),name='about')
]