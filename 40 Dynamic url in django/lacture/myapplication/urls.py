from django.urls import path
from myapplication import views

urlpatterns=[
    path('student/<my_id>/<int:id>',views.show_details,name='detail'),
    path('home/',views.homepage,{'check':'OK'},name='homepage')
]