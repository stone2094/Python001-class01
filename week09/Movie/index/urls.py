from django.urls import path, re_path, register_converter
from . import views  #, converters

urlpatterns = [
    ##path('', views.index),
    path('movies', views.movies),
    path('wrong_password', views.wrong_password),
    path('logged_in', views.logged_in),
    path('', views.login2)
]