from django.urls import path
from myapplication import views

urlpatterns=[
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_form,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout',views.user_logout,name='logout')
]