__author__ = 'Haoran'
from django.conf.urls import patterns, url

from BlogRater import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^get_author/', views.index, name='index')
]