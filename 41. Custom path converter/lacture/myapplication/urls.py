from django.urls import path,register_converter
from myapplication import views,converters
register_converter(converters.FourDigitYearConverter,'yyyy')
urlpatterns=[
    path('student/<yyyy:year>',views.show_details),
    
]