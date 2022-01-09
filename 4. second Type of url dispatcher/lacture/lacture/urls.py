"""lacture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapplication import views as mv
from secondapplication import views as sv
from thirdapplication import views as tv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include([
        path('learndjango/',mv.learn_django),
        path('learnpython/',mv.learn_python),
        path('learnvar/',mv.learn_var),
        path('learnmath/',mv.learn_math),
        path('learnformat/',mv.learn_format),
    ])),

    path('secondapplication/',include([
        path('secondapp/',sv.secondapp)
    ])),

    path('thirdapplication/',include([
        path('thirdapp/',tv.thirdapp)
    ]))
]
