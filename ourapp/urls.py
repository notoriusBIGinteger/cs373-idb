from django.conf.urls import patterns, url

from ourapp import views

urlpatterns = patterns('',
url(r'^dish/(?P<dishID>\d+)/$', views.dish, name='dish'),
url(r'^restaurant/(?P<restaurantID>\d+)/$', views.restaurant, name='restaurant'),
url(r'^customer/(?P<customerID>\d+)/$', views.customer, name='customer'),
url(r'^index/$', views.index, name='index'),
)
