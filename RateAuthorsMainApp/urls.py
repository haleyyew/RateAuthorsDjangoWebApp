__author__ = 'Haoran'
from django.conf.urls import patterns, url

from RateAuthorsMainApp import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))