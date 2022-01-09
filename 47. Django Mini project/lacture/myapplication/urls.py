from django.urls import path
from myapplication import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout',views.user_logout,name='logout'),
    path('blogpost/',views.blog_post,name='blogpost'),
    path('updatepost/<int:id>',views.update_post,name='update'),
    path('deletepost/<int:id>',views.Delete_post,name='delete'),
    path('passwordchange/',views.change_password,name='passwordchange')
]