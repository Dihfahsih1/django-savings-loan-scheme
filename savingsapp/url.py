from django.conf.urls import url, include
from django.contrib.auth.views import *
from django.urls import path
from savingsapp import views

urlpatterns = [
    url(r'^$', views.index, name='/'),
    ]
