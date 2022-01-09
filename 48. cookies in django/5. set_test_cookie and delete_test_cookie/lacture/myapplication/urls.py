from django.urls import path
from myapplication import views

urlpatterns=[
  path('set/',views.settestcookie),
  path('check/',views.checktestcookie),
  path('del/',views.deletetestcookie)
]