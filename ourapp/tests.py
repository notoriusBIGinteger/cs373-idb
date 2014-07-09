from django.test import TestCase
from ourapp.models import Cuisine, Restaurant, Customer, GenericDish, Dish, RestaurantReview, DishReview


class CuisineMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        c = Cuisine(name = "Italian")
        self.assertEqual(c.get_all(), {"name": "Italian"})

    def test_get_all_2(self):
        c = Cuisine(name = "Mexican")
        self.assertEqual(c.get_all(), {"name": "Mexican"})

    def test_get_all_3(self):
        c = Cuisine(name = "American")
        self.assertEqual(c.get_all(), {"name": "American"})

    # ---------
    # set_name
    # ---------
    def test_set_name_1(self):
        c = Cuisine(name = "Italian")
        self.assertEqual(c.name, "Italian")
        c.set_name("American")
        self.assertEqual(c.name, "American")

    def test_set_name_2(self):
        c = Cuisine(name = "Italian")
        self.assertEqual(c.name, "Italian")
        c.set_name("Mexican")
        self.assertEqual(c.name, "Mexican")

    def test_set_name_3(self):
        c = Cuisine(name = "Italian")
        self.assertEqual(c.name, "Italian")
        c.set_name("Asian")
        self.assertEqual(c.name, "Asian")

class RestaurantMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        r = Restaurant(name="Kerbey Lane",
                       reservation_required = False,
                       reservation_avail = False,
                       has_waiter = True,
                       phone_number = "5125555555",
                       description = "Diner Food",
                       zip_code = "78741",
                       address = "Austin",
                       delivery = False,
                       take_out = False,
                       pet_friendly = True,
                       cost = 2,
                       website = "http://fake.com")
        self.assertEqual(r.get_all(), {"name": "Kerbey Lane",
	                                   "reservation_required": False,
	                                   "reservation_avail": False,
	                                   "has_waiter": True,
	                                   "phone_number":"5125555555" ,
	                                   "description": "Diner Food",
	                                   "zip_code": "78741",
	                                   "address": "Austin",
	                                   "delivery":False,
	                                   "take_out":False,
	                                   "pet_friendly":True,
	                                   "cost":2,
	                                   "website":"http://fake.com"})
    def test_get_all_2(self):
        r = Restaurant(name="Magnolia Cafe",
                       reservation_required = False,
                       reservation_avail = False,
                       has_waiter = True,
                       phone_number = "5125555555",
                       description = "Diner",
                       zip_code = "78741",
                       address = "Austin",
                       delivery = False,
                       take_out = True,
                       pet_friendly = True,
                       cost = 2,
                       website = "http://fakewebsite.com")
        self.assertEqual(r.get_all(), {"name": "Magnolia Cafe",
	                                   "reservation_required": False,
	                                   "reservation_avail": False,
	                                   "has_waiter": True,
	                                   "phone_number":"5125555555" ,
	                                   "description": "Diner",
	                                   "zip_code": "78741",
	                                   "address": "Austin",
	                                   "delivery":False,
	                                   "take_out":True,
	                                   "pet_friendly":True,
	                                   "cost":2,
	                                   "website":"http://fakewebsite.com"})

    def test_get_all_3(self):
        r = Restaurant(name="Thai Spice",
                       reservation_required = False,
                       reservation_avail = True,
                       has_waiter = True,
                       phone_number = "5125555555",
                       description = "Asian",
                       zip_code = "78741",
                       address = "Austin",
                       delivery = True,
                       take_out = True,
                       pet_friendly = False,
                       cost = 2,
                       website = "http://2spicy4U.com")
        self.assertEqual(r.get_all(), {"name": "Thai Spice",
	                                   "reservation_required": False,
	                                   "reservation_avail": True,
	                                   "has_waiter": True,
	                                   "phone_number":"5125555555" ,
	                                   "description": "Asian",
	                                   "zip_code": "78741",
	                                   "address": "Austin",
	                                   "delivery":True,
	                                   "take_out":True,
	                                   "pet_friendly":False,
	                                   "cost":2,
	                                   "website":"http://2spicy4U.com"})

class CustomerMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        c = Customer(name = "Bobby")
        self.assertEqual(c.get_all(), {"name": "Bobby"})

    def test_get_all_2(self):
        c = Customer(name = "Sam")
        self.assertEqual(c.get_all(), {"name": "Sam"})

    def test_get_all_3(self):
        c = Customer(name = "Dean")
        self.assertEqual(c.get_all(), {"name": "Dean"})

class GenericDishMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        gd = GenericDish(name = "Hamburger")
        self.assertEqual(gd.get_all(), {"name":"Hamburger"})

    def test_get_all_2(self):
        gd = GenericDish(name = "Pizza")
        self.assertEqual(gd.get_all(), {"name":"Pizza"})

    def test_get_all_3(self):
        gd = GenericDish(name = "Sushi")
        self.assertEqual(gd.get_all(), {"name":"Sushi"})

class DishMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        d = Dish(name = "BLT Sandwhich",
                 rating = 2,
                 num_ratings = 3,
                 sum_of_ratings = 5,
                 vegetarian = False,
                 vegan = False,
                 kosher = False,
                 halal = False,
                 nut_allergy = True,
                 cost = 4)
        self.assertEqual(d.get_all(),{"name":"BLT Sandwhich",
                                      "rating":2,
                                      "num_ratings":3,
                                      "sum_of_ratings":5,
                                      "vegetarian":False,
                                      "vegan":False,
                                      "kosher":False,
                                      "halal":False,
                                      "nut_allergy":True,
                                      "cost" : 4})

    def test_get_all_2(self):
        d = Dish(name = "Beef Taco",
                 rating = 4,
                 num_ratings = 10,
                 sum_of_ratings = 6,
                 vegetarian = False,
                 vegan = False,
                 kosher = True,
                 halal = False,
                 nut_allergy = False,
                 cost = 2)
        self.assertEqual(d.get_all(),{"name":"Beef Taco",
                                      "rating":4,
                                      "num_ratings":10,
                                      "sum_of_ratings":6,
                                      "vegetarian":False,
                                      "vegan":False,
                                      "kosher":True,
                                      "halal":False,
                                      "nut_allergy":False,
                                      "cost" : 2})

    def test_get_all_3(self):
        d = Dish(name = "Pancake",
                 rating = 4,
                 num_ratings = 11,
                 sum_of_ratings = 8,
                 vegetarian = True,
                 vegan = True,
                 kosher = True,
                 halal = True,
                 nut_allergy = False,
                 cost = 3)
        self.assertEqual(d.get_all(),{"name":"Pancake",
                                      "rating":4,
                                      "num_ratings":11,
                                      "sum_of_ratings":8,
                                      "vegetarian":True,
                                      "vegan":True,
                                      "kosher":True,
                                      "halal":True,
                                      "nut_allergy":False,
                                      "cost" : 3})

class RestaurantReviewMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        rr = RestaurantReview(rating = 3, review_comment = "Okay")
        self.assertEqual(rr.get_all(), {"rating":3, "review_comment":"Okay"})

    def test_get_all_2(self):
        rr = RestaurantReview(rating = 4, review_comment = "")
        self.assertEqual(rr.get_all(), {"rating":4, "review_comment":""})

    def test_get_all_3(self):
        rr = RestaurantReview(rating = 1, review_comment = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium.")
        self.assertEqual(rr.get_all(), {"rating":1, "review_comment":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."})

class DishReviewMethodTests(TestCase):
    # --------
    # get_all
    # --------
    def test_get_all_1(self):
        dr = DishReview(rating = 3, review_comment = "Okay")
        self.assertEqual(dr.get_all(), {"rating":3, "review_comment":"Okay"})

    def test_get_all_2(self):
        dr = DishReview(rating = 1, review_comment = "")
        self.assertEqual(dr.get_all(), {"rating":1, "review_comment":""})

    def test_get_all_3(self):
        dr = DishReview(rating = 5, review_comment = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium.")
        self.assertEqual(dr.get_all(), {"rating":5, "review_comment":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."})

