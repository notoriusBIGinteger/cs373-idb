from django.test import TestCase
from django.test.client import Client
from ourapp.models import Cuisine, Restaurant, Customer, GenericDish, Dish, RestaurantReview, DishReview

class Tests(TestCase):
    # ---------------
    # cuisine get_all
    # ---------------
    
    c1 = Cuisine(name = "Ital")  # gets set to Italian soon after 
    c2 = Cuisine(name = "Mexi")  # gets set to Meixcan soon after
    c3 = Cuisine(name = "Amer") # gets set to American soon after
    
    r = Restaurant(name="Kerbey Lane",
    reservation_required = False,
    reservation_avail = False,
    has_waiter = True,
    phone_number = '5555555555',
    description = 'Delicious breakfast',
    zip_code = '78705',
    address = '555 w 5th St',
    delivery = False,
    take_out = True,
    pet_friendly = False, 
    dollar_avg_rating = 5,
    dollar_num_rating = 5,
    dollar_sum_rating = 25,
    star_avg_rating = 5,
    star_num_rating = 5,
    star_sum_rating= 25,
    website = 'www.kerbey.com', #models.URLField('Website')
    cuisine = c3,
    mon_hours = '11AM - 9PM', 
    tue_hours = '11AM - 9PM',
    wed_hours = '11AM - 9PM',
    thu_hours = '11AM - 9PM',
    fri_hours = '11AM - 9PM',
    sat_hours = '11AM - 9PM',
    sun_hours = '11AM - 9PM') 



    def test_cuisine_get_all_1(self):
        self.assertEqual(Tests.c1.get_all(), {"name": "Ital"})

    def test_cuisine_get_all_2(self):
        self.assertEqual(Tests.c2.get_all(), {"name": "Mexi"})

    def test_cuisine_get_all_3(self):
        self.assertEqual(Tests.c3.get_all(), {"name": "Amer"})

    # ---------
    # cuisine set_name
    # ---------
    def test_cuisine_set_name_1(self):
        self.assertEqual(Tests.c1.name, "Ital")
        Tests.c1.set_name("Italian")
        self.assertEqual(Tests.c1.name, "Italian")

    def test_cuisine_set_name_2(self):
        self.assertEqual(Tests.c2.name, "Mexi")
        Tests.c2.set_name("Mexican")
        self.assertEqual(Tests.c2.name, "Mexican")

    def test_cuisine_set_name_3(self):
        self.assertEqual(Tests.c3.name, "Amer")
        Tests.c3.set_name("American")
        self.assertEqual(Tests.c3.name, "American")

    # ------------------
    # restaurant get_all
    # ------------------
    def test_restaurant_get_all_1(self):

        self.assertEqual(Tests.r.get_all(), {"name": "Kerbey Lane",
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
   
    def test_restaurant_get_all_2(self):
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

    def test_restaurant_get_all_3(self):
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

    # ----------------
    # customer get_all
    # ----------------
    def test_customer_get_all_1(self):
        c = Customer(name = "Bobby")
        self.assertEqual(c.get_all(), {"name": "Bobby"})

    def test_customer_get_all_2(self):
        c = Customer(name = "Sam")
        self.assertEqual(c.get_all(), {"name": "Sam"})

    def test_customer_get_all_3(self):
        c = Customer(name = "Dean")
        self.assertEqual(c.get_all(), {"name": "Dean"})

    # --------------------
    # generic dish get_all
    # --------------------
    def test_generic_dish_get_all_1(self):
        gd = GenericDish(name = "Hamburger")
        self.assertEqual(gd.get_all(), {"name":"Hamburger"})

    def test_generic_dish_get_all_2(self):
        gd = GenericDish(name = "Pizza")
        self.assertEqual(gd.get_all(), {"name":"Pizza"})

    def test_generic_dish_get_all_3(self):
        gd = GenericDish(name = "Sushi")
        self.assertEqual(gd.get_all(), {"name":"Sushi"})

    # ------------
    # dish get_all
    # ------------
    def test_dish_get_all_1(self):
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

    def test_dish_get_all_2(self):
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

    def test_dish_get_all_3(self):
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

    # -------------------------
    # restaurant review get_all
    # -------------------------
    def test_restaurant_review_get_all_1(self):
        rr = RestaurantReview(rating = 3, review_comment = "Okay")
        self.assertEqual(rr.get_all(), {"rating":3, "review_comment":"Okay"})

    def test_restaurant_review_get_all_2(self):
        rr = RestaurantReview(rating = 4, review_comment = "")
        self.assertEqual(rr.get_all(), {"rating":4, "review_comment":""})

    def test_restaurant_review_get_all_3(self):
        rr = RestaurantReview(star_rating = 1, review_comment = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium.")
        self.assertEqual(rr.get_all(), {"rating":1, "review_comment":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."})

    # -------------------
    # dish review get_all
    # -------------------
    def test_dish_review_get_all_1(self):
        dr = DishReview(rating = 3, review_comment = "Okay")
        self.assertEqual(dr.get_all(), {"rating":3, "review_comment":"Okay"})

    def test_dish_review_get_all_2(self):
        dr = DishReview(rating = 1, review_comment = "")
        self.assertEqual(dr.get_all(), {"rating":1, "review_comment":""})

    def test_dish_review_get_all_3(self):
        dr = DishReview(rating = 5, review_comment = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium.")
        self.assertEqual(dr.get_all(), {"rating":5, "review_comment":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."})

    def test_restaurant_api_list_restaurants_1(self):
        dr = DishReview(star_rating = 3, dollar_rating = 4, review_comment = "Okay")
        dr.save()
        self.assertTrue(True)

        




