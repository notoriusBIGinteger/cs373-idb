from django.conf.urls import patterns, url, include

from ourapp import views

urlpatterns = patterns('',
url(r'^index/$', views.index, name='index'),
url(r'^restaurants/(json)?$', views.restaurant_list, name = 'restsjson'),
url(r'^restaurants/([0-9]+)/(json)?$', views.restaurant_detail, name = 'arestjson'),
url(r'^restaurants/([0-9]+)/dishes/(json)?$', views.restaurant_dishes, name = 'restdishjson'),
url(r'^restaurants/([0-9]+)/reviews/(json)?$', views.restaurant_reviews, name = 'restrevjson'),
url(r'^customers/(json)?$', views.customer_list, name = 'custsjson'),
url(r'^customers/([0-9]+)/(json)?$', views.customer_detail, name = 'acustjson'),
url(r'^customers/([0-9]+)/restaurantreviews/(json)?$', views.customer_restaurant_reviews, name = 'restrevsjson'),
url(r'^customers/([0-9]+)/dishreviews/(json)?$', views.customer_dish_reviews, name = 'dishrevsjson'),
url(r'^dishes/(json)?$', views.dish_list, name = 'dishesjson'),
url(r'^dishes/([0-9]+)/(json)?$', views.dish_detail, name = 'adishjson'),
url(r'^dishes/([0-9]+)/reviews/(json)?$', views.dish_reviews, name = 'dishesrevsjson'),
url(r'^genericdishes/(json)?$', views.generic_dish_list, name = 'gdishesjson'),
url(r'^genericdishes/([0-9]+)/(json)?$', views.generic_dish_detail, name = 'agdishjson'),
url(r'^genericdishes/([0-9]+)/dishes/(json)?$', views.generic_dish_dishes, name = 'agdishdishesjson'),
url(r'^cuisines/(json)?$', views.cuisine_list, name = 'cuisinesjson'),
url(r'^cuisines/([0-9]+)/(json)?$', views.cuisine_detail, name = 'acuisinejson'),
url(r'^cuisines/([0-9]+)/dishes/(json)?$', views.cuisine_dishes, name = 'acuisinesdishesjson'),
url(r'^cuisines/([0-9]+)/restaurants/(json)?$', views.cuisine_restaurants, name = 'acuisinesrestsjson'),
url(r'^about$', views.about, name = 'about'),
url(r'^splash/$', views.splash, name = 'splash'),
url(r'^theaustinites/$', views.the_austinites, name = 'austinites'),
url(r'^search/(.*)', views.search, name = 'search'),
)
