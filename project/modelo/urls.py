from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.fecha_actual,),
    url(r'^fecha/$', views.fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', views.horas_adelante),
]
