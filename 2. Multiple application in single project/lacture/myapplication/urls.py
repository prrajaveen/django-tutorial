


from django.urls import path
from myapplication import views
urlpatterns=[
    path('learndjango/',views.learn_django),
    path('learnpython/',views.learn_python),
    path('learnvar/',views.learn_var),
    path('learnmath/',views.learn_math),
    path('learnformat/',views.learn_format),
]