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
url(r'^customers/(?P<pk>[0-9]+)/$', views.customer_detail),
url(r'^customers/(?P<pk>[0-9]+)/restaurantreviews$', views.customer_restaurant_reviews),
url(r'^customers/(?P<pk>[0-9]+)/dishreviews$', views.customer_dish_reviews),
url(r'^dishes/$', views.dish_list),
url(r'^dishes/(?P<pk>[0-9]+)/$', views.dish_detail),
url(r'^dishes/(?P<pk>[0-9]+)/reviews$', views.dish_reviews),
url(r'^genericdishes/$', views.generic_dish_list),
url(r'^genericdishes/(?P<pk>[0-9]+)/$', views.generic_dish_detail),
url(r'^genericdishes/(?P<pk>[0-9]+)/dishes$', views.generic_dish_dishes),
url(r'^cuisines/$', views.cuisine_list),
url(r'^cuisines/(?P<pk>[0-9]+)/$', views.cuisine_detail),
url(r'^cuisines/(?P<pk>[0-9]+)/dishes$', views.cuisine_dishes),
url(r'^cuisines/(?P<pk>[0-9]+)/restaurants$', views.cuisine_restaurants),
url(r'^temp/temp$', views.temp),
url(r'^rest$', views.rest),
url(r'^nathantest$', views.nate_test),
url(r'^dish_temp/$', views.dish_temp),
url(r'splash/$', views.splash),
)
