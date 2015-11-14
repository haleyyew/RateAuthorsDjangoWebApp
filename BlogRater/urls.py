__author__ = 'Haoran'
from django.conf.urls import patterns, url

from BlogRater import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))