from django.urls import path

from . import views

app_name = 'sample_api_weathermap'
urlpatterns = [
    path('', views.sample_api_weathermap, name='sample_api_weathermap'),
    path('forecast', views.forecast, name='forecast'),
]