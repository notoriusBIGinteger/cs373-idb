from django.contrib import admin
from ourapp.models import Restaurant, Customer, Cuisine, GenericDish, Dish, RestaurantReview, DishReview

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Cuisine)
admin.site.register(GenericDish)
admin.site.register(Dish)
admin.site.register(RestaurantReview)
admin.site.register(DishReview)

# Register your models here.
