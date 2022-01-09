from django.urls import path
from myapplication import views

urlpatterns=[
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_form,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout',views.user_logout,name='logout'),
    path('changepassword/',views.user_change_password,name='changepassword'),
    path('withoutoldpassword/',views.user_change_password_without_old_password,name='withoutoldpassword'),
    path('userdetail/<int:id>',views.user_detail,name='userdetail')
]