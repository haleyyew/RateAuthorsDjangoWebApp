__author__ = 'Haoran'
from django.conf.urls import patterns, url

from BlogRater import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_author/', views.get_author, name='get_author'),
    url(r'^rate_author/', views.add_rating, name='rate_author')

]