from myapplication import views
from django.urls import path


urlpatterns=[
    path('',views.home),
    path('fees/',views.get_or_set),
    path('setmany/',views.set_many),
    path('delete/',views.deletecache),
    path('dec/',views.decrement_increment),
    path('clear/',views.cache_clear)


]