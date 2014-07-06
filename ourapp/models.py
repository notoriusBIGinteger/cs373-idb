from django.db import models

class Restaurant(models.Model) :
	name = models.CharField('Name', max_length=30)
	reservation_required = models.BooleanField('Reservations Required')
	reservation_avail = models.BooleanField('Reservations Available')
	has_waiter =models.CharField('Table Service', max_length=10)
	phone_number = models.CharField('Phone Number', max_length=50)
	food_type = models.CharField('Cuisine', max_length=30)
	zip_code = models.CharField('Zip Code', max_length=5)
	address = models.CharField('Address', max_length=50)
	delivery = models.BooleanField('Delivery Available')
	take_out = models.BooleanField('Take-out Available')
	pet_friendly = models.BooleanField('Pet Friendly')
	cost = models.IntegerField('Cost', max_length=1)
	website = models.URLField('Website')
	
	def __str__(self) : 
		return self.name
	
	class Meta:
		ordering = ["name"]

class Customer(models.Model) : 
	name = models.CharField('Customer Name', max_length=15)
	recent_check_in = models.CharField('Last Check-In', max_length=30)
	dietary_preference = models.CharField('Diet', max_length=60)
	
	def __str__(self) : 
		return self.name
		
class Dish(models.Model) : 
	name = models.CharField('Dish Name', max_length=20)
	rating = models.IntegerField('Avg. Rating', max_length=1)
	vegetarian = models.BooleanField('Vegetarian')
	vegan = models.BooleanField('Vegan')
	kosher = models.BooleanField('Kosher')
	halal = models.BooleanField('Halal')
	nut_allergy = models.BooleanField('Contains Nuts')
	#image = models.ImageField()
	price = models.IntegerField('Cost', max_length=1)
	restaurant = models.ForeignKey(Restaurant)
	generic_dish = models.ForeignKey(GenericDish)
	
	def __str__(self) : 
		return self.name

class RestaurantReview(models.Model) : 
	rating = models.IntegerField('Rating', max_length=1)
	review_comment = models.CharField('Comment', max_length=250)
	customer = models.ForeignKey(Customer)
	restaurant = models.ForeignKey(Restaurant)
	
	def __str__(self) : 
		return str(self.rating)

class DishReview(models.Model) : 
	rating = models.IntegerField('Rating', max_length=1)
	review_comment = models.CharField('Comment', max_length=250)
	customer = models.ForeignKey(Customer)
	dish = models.ForeignKey(Dish)
	
	def __str__(self) : 
		return str(self.rating)		
	
class Cuisine(models.Model) : 
	name = models.CharField('Comment', max_length=30)
	
	def __str__(self) : 
		return str(self.rating)	
		
class GenericDish(models.Model) : 
	name = models.CharField('Comment', max_length=30)
	cuisine = models.ForeignKey(Cuisine)
	
	def __str__(self) : 
		return self.name	