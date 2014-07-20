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

    class Meta:
        app_label = 'notoriousBIGinteger'

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"name":self.name}

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
    cost = models.IntegerField('Cost', max_length=1)
    website = models.URLField('Website')
    cuisine = models.ForeignKey(Cuisine)

    def __str__(self) :
        return self.name

    class Meta:
        ordering = ["name"]
        app_label = 'notoriousBIGinteger'

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"name": self.name,
                "reservation_required": self.reservation_required,
                "reservation_avail": self.reservation_avail ,
                "has_waiter": self.has_waiter,
                "phone_number": self.phone_number,
                "description": self.description,
                "zip_code": self.zip_code,
                "address": self.address,
                "delivery":self.delivery,
                "take_out":self.take_out,
                "pet_friendly":self.pet_friendly,
                "cost":self.cost,
                "website":self.website}

"""
Customer containts a full name of a reviewer
"""
class Customer(models.Model) :
    name = models.CharField('Name', max_length=35)
    #recent_check_in = models.CharField('Last Check-In', max_length=30)
    #dietary_preference = models.CharField('Diet', max_length=60)

    def __str__(self) :
        return self.name

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"name":self.name}
    class Meta:
        app_label = 'notoriousBIGinteger'

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
        return { "name" : self.name }

    class Meta:
        app_label = 'notoriousBIGinteger'

"""
Dish contains two foreign keys of a restaurant and a generic dish
and descriptive attributes of a meal.
"""
class Dish(models.Model) :
    name = models.CharField('Name', max_length=40)
    rating = models.IntegerField('Avg. Rating', max_length=1)
    num_ratings = models.IntegerField('Number of Ratings')
    sum_of_ratings = models.IntegerField() # customers shouldn't see this.
    vegetarian = models.BooleanField('Vegetarian')
    vegan = models.BooleanField('Vegan')
    kosher = models.BooleanField('Kosher')
    halal = models.BooleanField('Halal')
    nut_allergy = models.BooleanField('Contains Nuts')
    #image = models.ImageField()
    cost = models.IntegerField('Cost', max_length=1)
    restaurant = models.ForeignKey(Restaurant)
    generic_dish = models.ForeignKey(GenericDish)

    def __str__(self) :
        return self.name

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"name": self.name,
                "rating": self.rating,
                "num_ratings":self.num_ratings,
                "sum_of_ratings":self.sum_of_ratings,
                "vegetarian":self.vegetarian,
                "vegan":self.vegan,
                "kosher":self.kosher,
                "halal":self.halal,
                "nut_allergy":self.nut_allergy,
                "cost":self.cost}

    class Meta:
        app_label = 'notoriousBIGinteger'

"""
Restaurant Review contains two foreign keys from Customer and Restaurant
has a rating (int) and comment(str)
"""
class RestaurantReview(models.Model) :
    rating = models.IntegerField('Rating', max_length=1)
    review_comment = models.CharField('Comment', max_length=250)
    customer = models.ForeignKey(Customer)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self) :
        return str(self.rating)

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"rating": self.rating,
                "review_comment":self.review_comment}
    class Meta:
        app_label = 'notoriousBIGinteger'

"""
Dish Review contains two foreign keys from Customer and Dish
has a rating (int) and comment(str)
"""
class DishReview(models.Model) :
    rating = models.IntegerField('Rating', max_length=1)
    review_comment = models.CharField('Comment', max_length=250)
    customer = models.ForeignKey(Customer)
    dish = models.ForeignKey(Dish)

    def __str__(self) :
        return str(self.rating)
    class Meta:
        app_label = 'notoriousBIGinteger'

    def get_all(self):
        """
        returns all of the elements in the class
        in a dictionary with key being the attribute name
        and value being the value of the attribute
        """
        return {"rating": self.rating,
                "review_comment":self.review_comment}
