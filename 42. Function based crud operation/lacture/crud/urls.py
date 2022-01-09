from django.urls import path
from crud import views


urlpatterns=[
    path('',views.home,name='home'),
    path('registration/',views.registration,name='registration'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]