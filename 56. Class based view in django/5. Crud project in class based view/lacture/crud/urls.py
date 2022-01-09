from django.urls import path
from crud import views


urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    # path('registration/',views.registration,name='registration'),
    path('update/<int:id>',views.Studentupdate.as_view(),name='update'),
    path('delete/<int:id>',views.StudentDelete.as_view(),name='delete')
]