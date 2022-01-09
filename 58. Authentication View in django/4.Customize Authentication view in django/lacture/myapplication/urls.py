from django.urls import path
from django.views.generic.base import TemplateView
from myapplication import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_view



urlpatterns=[
    path('login/',views.MyLoginView.as_view(),name='login'),
    path('dashboard/',TemplateView.as_view(template_name='myapplication/dashboard.html'),name='dashboard'),
    path('raja/',auth_view.LogoutView.as_view(template_name='myapplication/logout.html'),name='logout'),
    path('changepass/',auth_view.PasswordChangeView.as_view(template_name='myapplication/password_change.html',success_url='/changepassdone/'),name='changepass'),
    path('changepassdone/',auth_view.PasswordChangeDoneView.as_view(template_name='myapplication/changepassdone.html'),name='changepassdone')

]