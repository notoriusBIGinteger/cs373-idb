from django.db import models

"""
Cuisine is the top most level in our hierarchy
it is for names such as Italian, Mexian, ...
"""
class Cuisine(models.Model) :
    name = models.CharField('Name', max_length=30)

    def __str__(self) :
        return str(self.name)

    def set_name(self, name):
        self.name = name


    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"name":self.name}

    def getDict(self) :
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return ({ 'id' : self.id, 'name' : self.name})
"""
Restaurant model has a foreign key of Cuisine
and attributes that describes an actual Restaurant
"""
class Restaurant(models.Model) :
    name = models.CharField('Name', max_length=30)
    reservation_required = models.BooleanField('Reservations Required')
    reservation_avail = models.BooleanField('Reservations Available')
    has_waiter =models.BooleanField('Waiter Service')
    phone_number = models.CharField('Phone Number', max_length=10)
    description = models.CharField('Description', max_length=200)
    zip_code = models.CharField('Zip Code', max_length=5)
    address = models.CharField('Address', max_length=50)
    delivery = models.BooleanField('Delivery Available')
    take_out = models.BooleanField('Take-out Available')
    pet_friendly = models.BooleanField('Pet Friendly')
    dollar_avg_rating = models.FloatField()
    dollar_num_rating =models.IntegerField()
    dollar_sum_rating=models.IntegerField()
    star_avg_rating = models.FloatField()
    star_num_rating =models.IntegerField()
    star_sum_rating=models.IntegerField()
    website = models.URLField('Website')
    cuisine = models.ForeignKey(Cuisine)
    mon_hours = models.CharField('Monday Hours', max_length=100)
    tue_hours = models.CharField('Tuesday Hours', max_length=100)
    wed_hours = models.CharField('Thursday Hours', max_length=100)
    thu_hours = models.CharField('Wednesday Hours', max_length=100)
    fri_hours = models.CharField('Friday Hours', max_length=100)
    sat_hours = models.CharField('Saturday Hours', max_length=100)
    sun_hours = models.CharField('Sunday Hours', max_length=100)

    def __str__(self) :
        return self.name


    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
                'name' : self.name,
                'reservation_required' : self.reservation_required ,
                'reservation_avail' :  self.reservation_avail ,
                'has_waiter' : self.has_waiter ,
                'phone_number' : self.phone_number ,
                'description' : self.description,
                'zip_code' : self.zip_code,
                'address' : self.address,
                'delivery' : self.delivery,
                'take_out' : self.take_out,
                'pet_friendly' : self.pet_friendly,
                'dollar_avg_rating' : self.dollar_avg_rating,
                'dollar_num_rating' : self.dollar_num_rating,
                'dollar_sum_rating' : self.dollar_sum_rating,
                'star_avg_rating' : self.star_avg_rating,
                'star_num_rating' : self.star_num_rating,
                'star_sum_rating' : self.star_sum_rating,
                'website' : self.website,
                'cuisine' : self.cuisine,
                'mon_hours' : self.mon_hours,
                'tue_hours' : self.tue_hours,
                'wed_hours' : self.wed_hours,
                'thu_hours' : self.thu_hours,
                'fri_hours' : self.fri_hours,
                'sat_hours' : self.sat_hours,
                'sun_hours' : self.sun_hours
                }

    def getDict(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
                'id' : self.id,
                'name' : self.name,
                'reservation_required' : self.reservation_required ,
                'reservation_avail' :  self.reservation_avail ,
                'has_waiter' : self.has_waiter ,
                'phone_number' : self.phone_number ,
                'description' : self.description,
                'zip_code' : self.zip_code,
                'address' : self.address,
                'delivery' : self.delivery,
                'take_out' : self.take_out,
                'pet_friendly' : self.pet_friendly,
                'dollar_avg_rating' : self.dollar_avg_rating,
                'dollar_num_rating' : self.dollar_num_rating,
                'dollar_sum_rating' : self.dollar_sum_rating,
                'star_avg_rating' : self.star_avg_rating,
                'star_num_rating' : self.star_num_rating,
                'star_sum_rating' : self.star_sum_rating,
                'website' : self.website,
                'cuisine_id' : self.cuisine.id,
                'mon_hours' : self.mon_hours,
                'tue_hours' : self.tue_hours,
                'wed_hours' : self.wed_hours,
                'thu_hours' : self.thu_hours,
                'fri_hours' : self.fri_hours,
                'sat_hours' : self.sat_hours,
                'sun_hours' : self.sun_hours
                }

"""
Customer containts a full name of a reviewer
"""
class Customer(models.Model) :
    name = models.CharField('Name', max_length=35)
    description = models.CharField('Description', max_length=100)

    def __str__(self) :
        return self.name

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"name" : self.name, "description" : self.description }

    def getDict(self) :
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"id" : self.id, "name" : self.name, "description" : self.description}

"""
Generic Dish has a foreign key Cuisine
and a name of a generic dish ie Pizza, Taco
"""
class GenericDish(models.Model) :
    name = models.CharField('Name', max_length=30)
    cuisine = models.ForeignKey(Cuisine)

    def __str__(self) :
        return self.name

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return { "name" : self.name, 'cuisine' : self.cuisine }

    def getDict(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return { 'id' : self.id, 'name' : self.name, 'cuisine_id' : self.cuisine.id }

"""
Dish contains two foreign keys of a restaurant and a generic dish
and descriptive attributes of a meal.
"""
class Dish(models.Model) :
    name = models.CharField('Name', max_length=40)
    star_avg_rating = models.FloatField(max_length=1)
    star_num_ratings = models.IntegerField()
    star_sum_ratings = models.IntegerField() # customers shouldn't see this.
    dollar_avg_rating = models.FloatField(max_length=1)
    dollar_num_ratings = models.IntegerField()
    dollar_sum_ratings = models.IntegerField()
    vegetarian = models.BooleanField('Vegetarian')
    vegan = models.BooleanField('Vegan')
    kosher = models.BooleanField('Kosher')
    halal = models.BooleanField('Halal')
    nut_allergy = models.BooleanField('Contains Nuts')
    #image = models.ImageField()
    restaurant = models.ForeignKey(Restaurant)
    generic_dish = models.ForeignKey(GenericDish)
    cuisine = models.ForeignKey(Cuisine)
    description = models.CharField('Description', max_length=300)

    def __str__(self) :
        return self.name

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
               'name' : self.name,
               'star_avg_rating' : self.star_avg_rating,
               'star_num_ratings' : self.star_num_ratings,
               'star_sum_ratings' : self.star_sum_ratings,
               'dollar_avg_rating' : self.dollar_avg_rating,
               'dollar_num_ratings' : self.dollar_num_ratings,
               'dollar_sum_ratings' : self.dollar_sum_ratings,
               'vegetarian' : self.vegetarian,
               'vegan' : self.vegan,
               'kosher' : self.kosher,
               'halal' : self.halal,
               'nut_allergy' : self.nut_allergy,
               'restaurant' : self.restaurant,
               'generic_dish' : self.generic_dish,
               'cuisine' : self.cuisine,
               'description' : self.description
               }

    def getDict(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
               'id' : self.id,
               'name' : self.name,
               'star_avg_rating' : self.star_avg_rating,
               'star_num_ratings' : self.star_num_ratings,
               'star_sum_ratings' : self.star_sum_ratings,
               'dollar_avg_rating' : self.dollar_avg_rating,
               'dollar_num_ratings' : self.dollar_num_ratings,
               'dollar_sum_ratings' : self.dollar_sum_ratings,
               'vegetarian' : self.vegetarian,
               'vegan' : self.vegan,
               'kosher' : self.kosher,
               'halal' : self.halal,
               'nut_allergy' : self.nut_allergy,
               'restaurant_id' : self.restaurant.id,
               'generic_dish_id' : self.generic_dish.id,
               'cuisine_id' : self.cuisine.id,
               'description' : self.description
               }


"""
Restaurant Review contains two foreign keys from Customer and Restaurant
has a rating (int) and comment(str)
"""
class RestaurantReview(models.Model) :
    star_rating = models.IntegerField('Star Rating', max_length=1)
    dollar_rating = models.IntegerField('Price Rating', max_length=1)
    review_comment = models.CharField('Comment', max_length=250)
    customer = models.ForeignKey(Customer)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self) :
        return str(self.customer) + "-" + str(self.restaurant)

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
                "star_rating": self.star_rating,
                "dollar_rating":self.dollar_rating,
                "review_comment":self.review_comment,
                'customer' : self.customer,
                'restaurant' : self.restaurant
                }

    def getDict(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
                "id" : self.id,
                "star_rating": self.star_rating,
                "dollar_rating":self.dollar_rating,
                "review_comment":self.review_comment,
                'customer_id' : self.customer.id,
                'restaurant_id' : self.restaurant.id
                }

"""
Dish Review contains two foreign keys from Customer and Dish
has a rating (int) and comment(str)
"""
class DishReview(models.Model) :
    star_rating = models.IntegerField('Star Rating', max_length=1)
    dollar_rating = models.IntegerField('Dollar Rating', max_length=1)
    review_comment = models.CharField('Comment', max_length=250)
    customer = models.ForeignKey(Customer)
    dish = models.ForeignKey(Dish)

    def __str__(self) :
        return str(self.customer) + "-" + str(self.dish)

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {'star_rating' : self.star_rating,
                'dollar_rating' : self.dollar_rating,
                'review_comment' : self.review_comment,
                'customer' : self.customer,
                'dish' : self.dish
               }

    def getDict(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {
                'id' : self.id,
                'star_rating' : self.star_rating,
                'dollar_rating' : self.dollar_rating,
                'review_comment' : self.review_comment,
                'customer_id' : self.customer.id,
                'dish_id' : self.dish.id
               }
