'''
Created on 30-Sep-2016

@author: hgupta
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]