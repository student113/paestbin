from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^ajax', views.ajax, name="ajax"),
    url(r'^getajax', views.getajax, name="getajax"),
]