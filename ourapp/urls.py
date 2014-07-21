from django.conf.urls import patterns, url

from ourapp import views

urlpatterns = patterns('',
url(r'^dish/(?P<dishID>\d+)/$', views.dish, name='dish'),
url(r'^restaurant/(?P<restaurantID>\d+)/$', views.restaurant, name='restaurant'),
url(r'^customer/(?P<customerID>\d+)/$', views.customer, name='customer'),
url(r'^index/$', views.index, name='index'),
url(r'^restaurants/$', views.restaurant_list),
url(r'^restaurants/(?P<pk>[0-9]+)/$', views.restaurant_detail),
url(r'^restaurants/(?P<pk>[0-9]+)/dishes$', views.restaurant_dishes),
url(r'^restaurants/(?P<pk>[0-9]+)/reviews$', views.restaurant_reviews),
url(r'^customers/$', views.customer_list),
url(r'^customers/(?P<pk>[0-9]+)/attributes$', views.customer_detail),
url(r'^customers/(?P<pk>[0-9]+)/restaurantreviews$', views.customer_restaurant_reviews),
url(r'^customers/(?P<pk>[0-9]+)/dishreviews$', views.customer_dish_reviews),
)
