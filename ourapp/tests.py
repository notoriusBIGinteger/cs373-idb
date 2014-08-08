import re
import json
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from ourapp.models import Cuisine, Restaurant, Customer, GenericDish, Dish, RestaurantReview, DishReview

class Tests(TestCase):


    # ---------------
    # cuisine get_all
    # ---------------

    c1 = Cuisine(name = "Ital")  # gets set to Italian soon after
    c2 = Cuisine(name = "Mexi")  # gets set to Meixcan soon after
    c3 = Cuisine(name = "Amer") # gets set to American soon after

    r1 = Restaurant(
    name = "Kerbey Lane",
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
    star_sum_rating = 25,
    cuisine = c3,
    mon_hours = '11AM - 9PM',
    tue_hours = '11AM - 9PM',
    wed_hours = '11AM - 9PM',
    thu_hours = '11AM - 9PM',
    fri_hours = '11AM - 9PM',
    sat_hours = '11AM - 9PM',
    sun_hours = '11AM - 9PM',
    website = 'www.kerbey.com',
    )

    r2 = Restaurant(
    name = "Magnolia",
    reservation_required = True,
    reservation_avail = False,
    has_waiter = False,
    phone_number = '5554445555',
    description = 'Amazing breakfast',
    zip_code = '78705',
    address = '555 w 5th St',
    delivery = False,
    take_out = True,
    pet_friendly = False,
    dollar_avg_rating = 6,
    dollar_num_rating = 6,
    dollar_sum_rating = 36,
    star_avg_rating = 4,
    star_num_rating = 4,
    star_sum_rating = 16,
    cuisine = c3,
    mon_hours = '9AM - 10PM',
    tue_hours = '9AM - 10PM',
    wed_hours = '9AM - 10PM',
    thu_hours = '9AM - 10PM',
    fri_hours = '9AM - 10PM',
    sat_hours = '9AM - 10PM',
    sun_hours = '9AM - 10PM',
    website = 'www.MangoliaCafe.com',
    )


    r3 = Restaurant(
    name = "Big Bite",
    reservation_required = False,
    reservation_avail = False,
    has_waiter = True,
    phone_number = '1234445555',
    description = 'Amazing pizza',
    zip_code = '78705',
    address = '523 w 5th St',
    delivery = False,
    take_out = True,
    pet_friendly = True,
    dollar_avg_rating = 7,
    dollar_num_rating = 7,
    dollar_sum_rating = 49,
    star_avg_rating = 2,
    star_num_rating = 2,
    star_sum_rating = 4,
    cuisine = c1,
    mon_hours = '9AM - 10PM',
    tue_hours = '9AM - 10PM',
    wed_hours = '9AM - 10PM',
    thu_hours = '9AM - 10PM',
    fri_hours = '9AM - 10PM',
    sat_hours = '9AM - 10PM',
    sun_hours = '9AM - 10PM',
    website = 'www.BigBite.com'
    )

    cu1 = Customer(name = "Bobby", description = "cool")
    cu2 = Customer(name = "Sam", description = "ok")
    cu3 = Customer(name = "Jake", description = "nice")
    gd1 = GenericDish(name = "Hamburger", cuisine = c3)
    gd2 = GenericDish(name = "Pizza", cuisine = c1)
    gd3 = GenericDish(name = "Sushi", cuisine = c3)

    d1 = Dish(
    name = 'Trifecta Pizza',
    star_avg_rating = 4,
    star_num_ratings = 4,
    star_sum_ratings = 16,
    dollar_avg_rating = 3 ,
    dollar_num_ratings = 3,
    dollar_sum_ratings = 9,
    vegetarian = False,
    vegan = False,
    kosher = False,
    halal = False,
    nut_allergy = False,
    restaurant = r3,
    generic_dish = gd2,
    cuisine = c1,
    description = 'A trifecta of 3 meats including bacon'
    )

    d2 = Dish(
    name = 'Bacon Cheezburger',
    star_avg_rating = 5,
    star_num_ratings = 5,
    star_sum_ratings = 25,
    dollar_avg_rating = 2 ,
    dollar_num_ratings = 5,
    dollar_sum_ratings = 10,
    vegetarian = False,
    vegan = False,
    kosher = False,
    halal = False,
    nut_allergy = False,
    restaurant = r1,
    generic_dish = gd1,
    cuisine = c1,
    description = 'Bacon with some cheezburger on it'
    )

    d3 = Dish(
    name = 'White Roll',
    star_avg_rating = 3,
    star_num_ratings = 7,
    star_sum_ratings = 21,
    dollar_avg_rating = 2 ,
    dollar_num_ratings = 7,
    dollar_sum_ratings = 14,
    vegetarian = False,
    vegan = False,
    kosher = False,
    halal = False,
    nut_allergy = False,
    restaurant = r2,
    generic_dish = gd3,
    cuisine = c1,
    description = 'Prime sushi'
    )

    rr1 = RestaurantReview(
    star_rating = 1,
    dollar_rating = 5,
    review_comment = 'The food here stinks',
    customer = cu1,
    restaurant = r1,
    )

    rr2 = RestaurantReview(
    star_rating = 5,
    dollar_rating = 1,
    review_comment = 'The food here da bomb dot com.',
    customer = cu2,
    restaurant = r2,
    )

    rr3 = RestaurantReview(
    star_rating = 3,
    dollar_rating = 3,
    review_comment = 'The food here is alright.',
    customer = cu3,
    restaurant = r3,
    )

    dr1 = DishReview(
    star_rating = 2,
    dollar_rating = 4,
    review_comment = 'Meh.',
    customer = cu1 ,
    dish = d1
    )

    dr2 = DishReview(
    star_rating = 5,
    dollar_rating = 2,
    review_comment = 'I love bacon! I love this burger!',
    customer = cu2,
    dish = d2
    )

    dr3 = DishReview(
    star_rating = 3,
    dollar_rating = 4,
    review_comment = 'Its ok but its a little expensive.',
    customer = cu3,
    dish = d3,
    )

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

        self.assertEqual(Tests.r1.get_all(),  {'name' : "Kerbey Lane",
            'reservation_required' : False,
            'reservation_avail' : False,
            'has_waiter' : True,
            'phone_number' : '5555555555',
            'description' : 'Delicious breakfast',
            'zip_code' : '78705',
            'address' : '555 w 5th St',
            'delivery' : False,
            'take_out' : True,
            'pet_friendly' : False,
            'dollar_avg_rating' : 5,
            'dollar_num_rating' : 5,
            'dollar_sum_rating' : 25,
            'star_avg_rating' : 5,
            'star_num_rating' : 5,
            'star_sum_rating' : 25,
            'cuisine' : Tests.c3,
            'mon_hours' : '11AM - 9PM',
            'tue_hours' : '11AM - 9PM',
            'wed_hours' : '11AM - 9PM',
            'thu_hours' : '11AM - 9PM',
            'fri_hours' : '11AM - 9PM',
            'sat_hours' : '11AM - 9PM',
            'sun_hours' : '11AM - 9PM',
            'website' : 'www.kerbey.com' })

    def test_restaurant_get_all_2(self):
        self.assertEqual(Tests.r2.get_all(), {'name' : "Magnolia",
            'reservation_required' : True,
            'reservation_avail' : False,
            'has_waiter' : False,
            'phone_number' : '5554445555',
            'description' : 'Amazing breakfast',
            'zip_code' : '78705',
            'address' : '555 w 5th St',
            'delivery' : False,
            'take_out' : True,
            'pet_friendly' : False,
            'dollar_avg_rating' : 6,
            'dollar_num_rating' : 6,
            'dollar_sum_rating' : 36,
            'star_avg_rating' : 4,
            'star_num_rating' : 4,
            'star_sum_rating' : 16,
            'cuisine' : Tests.c3,
            'mon_hours' : '9AM - 10PM',
            'tue_hours' : '9AM - 10PM',
            'wed_hours' : '9AM - 10PM',
            'thu_hours' : '9AM - 10PM',
            'fri_hours' : '9AM - 10PM',
            'sat_hours' : '9AM - 10PM',
            'sun_hours' : '9AM - 10PM',
            'website' : 'www.MangoliaCafe.com',
            })

    def test_restaurant_get_all_3(self):
        self.assertEqual(Tests.r3.get_all(), {'name' : "Big Bite",
            'reservation_required' : False,
            'reservation_avail' : False,
            'has_waiter' : True,
            'phone_number' : '1234445555',
            'description' : 'Amazing pizza',
            'zip_code' : '78705',
            'address' : '523 w 5th St',
            'delivery' : False,
            'take_out' : True,
            'pet_friendly' : True,
            'dollar_avg_rating' : 7,
            'dollar_num_rating' : 7,
            'dollar_sum_rating' : 49,
            'star_avg_rating' : 2,
            'star_num_rating' : 2,
            'star_sum_rating' : 4,
            'cuisine' : Tests.c1,
            'mon_hours' : '9AM - 10PM',
            'tue_hours' : '9AM - 10PM',
            'wed_hours' : '9AM - 10PM',
            'thu_hours' : '9AM - 10PM',
            'fri_hours' : '9AM - 10PM',
            'sat_hours' : '9AM - 10PM',
            'sun_hours' : '9AM - 10PM',
            'website' : 'www.BigBite.com'
            })

    # ----------------
    # customer get_all
    # ----------------
    def test_customer_get_all_1(self):
        self.assertEqual(Tests.cu1.get_all(), {"name": "Bobby", 'description' : "cool"})

    def test_customer_get_all_2(self):
        self.assertEqual(Tests.cu2.get_all(), {"name": "Sam", 'description' : "ok"})

    def test_customer_get_all_3(self):
        self.assertEqual(Tests.cu3.get_all(), {"name": "Jake", 'description' : "nice"})

    # --------------------
    # generic dish get_all
    # --------------------
    def test_generic_dish_get_all_1(self):
        self.assertEqual(Tests.gd1.get_all(), {"name":"Hamburger", 'cuisine' : Tests.c3})

    def test_generic_dish_get_all_2(self):
        self.assertEqual(Tests.gd2.get_all(), {"name":"Pizza", 'cuisine' : Tests.c1})

    def test_generic_dish_get_all_3(self):
        self.assertEqual(Tests.gd3.get_all(), {"name":"Sushi", 'cuisine' : Tests.c3})

    # ------------
    # dish get_all
    # ------------
    def test_dish_get_all_1(self):
        self.assertEqual(Tests.d1.get_all(),{'name' : 'Trifecta Pizza',
            'star_avg_rating' : 4,
            'star_num_ratings' : 4,
            'star_sum_ratings' : 16,
            'dollar_avg_rating' : 3 ,
            'dollar_num_ratings' : 3,
            'dollar_sum_ratings' : 9,
            'vegetarian' : False,
            'vegan' : False,
            'kosher' : False,
            'halal' : False,
            'nut_allergy' : False,
            'restaurant' : Tests.r3,
            'generic_dish' : Tests.gd2,
            'cuisine' : Tests.c1,
            'description' : 'A trifecta of 3 meats including bacon'})

    def test_dish_get_all_2(self):
        self.assertEqual(Tests.d2.get_all(),{'name' : 'Bacon Cheezburger',
        'star_avg_rating' : 5,
        'star_num_ratings' : 5,
        'star_sum_ratings' : 25,
        'dollar_avg_rating' : 2 ,
        'dollar_num_ratings' : 5,
        'dollar_sum_ratings' : 10,
        'vegetarian' : False,
        'vegan' : False,
        'kosher' : False,
        'halal' : False,
        'nut_allergy' : False,
        'restaurant' : Tests.r1,
        'generic_dish' : Tests.gd1,
        'cuisine' : Tests.c1,
        'description' : 'Bacon with some cheezburger on it' })

    def test_dish_get_all_3(self):
        self.assertEqual(Tests.d3.get_all(),{'name' : 'White Roll',
        'star_avg_rating' : 3,
        'star_num_ratings' : 7,
        'star_sum_ratings' : 21,
        'dollar_avg_rating' : 2 ,
        'dollar_num_ratings' : 7,
        'dollar_sum_ratings' : 14,
        'vegetarian' : False,
        'vegan' : False,
        'kosher' : False,
        'halal' : False,
        'nut_allergy' : False,
        'restaurant' : Tests.r2,
        'generic_dish' : Tests.gd3,
        'cuisine' : Tests.c1,
        'description' : 'Prime sushi'})

    # -------------------------
    # restaurant review get_all
    # -------------------------
    def test_restaurant_review_get_all_1(self):
        self.assertEqual(Tests.rr1.get_all(), {'star_rating' : 1,
            'dollar_rating' : 5,
            'review_comment' : 'The food here stinks',
            'customer' : Tests.cu1,
            'restaurant' : Tests.r1
            })

    def test_restaurant_review_get_all_2(self):
        self.assertEqual(Tests.rr2.get_all(), {
            'star_rating' : 5,
            'dollar_rating' : 1,
            'review_comment' : 'The food here da bomb dot com.',
            'customer' : Tests.cu2,
            'restaurant' : Tests.r2,
            })

    def test_restaurant_review_get_all_3(self):
        self.assertEqual(Tests.rr3.get_all(), {
            'star_rating' : 3,
            'dollar_rating' : 3,
            'review_comment' : 'The food here is alright.',
            'customer' : Tests.cu3,
            'restaurant' : Tests.r3
            })

    # -------------------
    # dish review get_all
    # -------------------
    def test_dish_review_get_all_1(self):
        self.assertEqual(Tests.dr1.get_all(), {
            'star_rating' : 2,
            'dollar_rating' : 4,
            'review_comment' : 'Meh.',
            'customer' : Tests.cu1 ,
            'dish' : Tests.d1
            })

    def test_dish_review_get_all_2(self):
        self.assertEqual(Tests.dr2.get_all(), {
            'star_rating' : 5,
            'dollar_rating' : 2,
            'review_comment' : 'I love bacon! I love this burger!',
            'customer' : Tests.cu2 ,
            'dish' : Tests.d2
            })

    def test_dish_review_get_all_3(self):
        self.assertEqual(Tests.dr3.get_all(), {
            'star_rating' : 3,
            'dollar_rating' : 4,
            'review_comment' : 'Its ok but its a little expensive.',
            'customer' : Tests.cu3 ,
            'dish' : Tests.d3
            })

    def test_cuisine_get_dict_1(self):
        self.assertEqual(Tests.c1.getDict(), {"name": "Ital" , "id" : Tests.c1.id})

    def test_cuisine_get_dict_2(self):
        self.assertEqual(Tests.c2.getDict(), {"name": "Mexi" , "id" : Tests.c2.id})

    def test_cuisine_get_dict_3(self):
        self.assertEqual(Tests.c3.getDict(), {"name": "Amer" , "id" : Tests.c3.id})

    # ------------------
    # restaurant get_dict
    # ------------------
    def test_restaurant_get_dict_1(self):

        self.assertEqual(Tests.r1.getDict(),  {
            'id' : Tests.r1.id,
            'name' : "Kerbey Lane",
            'reservation_required' : False,
            'reservation_avail' : False,
            'has_waiter' : True,
            'phone_number' : '5555555555',
            'description' : 'Delicious breakfast',
            'zip_code' : '78705',
            'address' : '555 w 5th St',
            'delivery' : False,
            'take_out' : True,
            'pet_friendly' : False,
            'dollar_avg_rating' : 5,
            'dollar_num_rating' : 5,
            'dollar_sum_rating' : 25,
            'star_avg_rating' : 5,
            'star_num_rating' : 5,
            'star_sum_rating' : 25,
            'cuisine_id' : Tests.c3.id,
            'mon_hours' : '11AM - 9PM',
            'tue_hours' : '11AM - 9PM',
            'wed_hours' : '11AM - 9PM',
            'thu_hours' : '11AM - 9PM',
            'fri_hours' : '11AM - 9PM',
            'sat_hours' : '11AM - 9PM',
            'sun_hours' : '11AM - 9PM',
            'website' : 'www.kerbey.com' })

    def test_restaurant_get_dict_2(self):
        self.assertEqual(Tests.r2.getDict(), {'name' : "Magnolia",
            'id' : Tests.r2.id,
            'reservation_required' : True,
            'reservation_avail' : False,
            'has_waiter' : False,
            'phone_number' : '5554445555',
            'description' : 'Amazing breakfast',
            'zip_code' : '78705',
            'address' : '555 w 5th St',
            'delivery' : False,
            'take_out' : True,
            'pet_friendly' : False,
            'dollar_avg_rating' : 6,
            'dollar_num_rating' : 6,
            'dollar_sum_rating' : 36,
            'star_avg_rating' : 4,
            'star_num_rating' : 4,
            'star_sum_rating' : 16,
            'cuisine_id' : Tests.c3.id,
            'mon_hours' : '9AM - 10PM',
            'tue_hours' : '9AM - 10PM',
            'wed_hours' : '9AM - 10PM',
            'thu_hours' : '9AM - 10PM',
            'fri_hours' : '9AM - 10PM',
            'sat_hours' : '9AM - 10PM',
            'sun_hours' : '9AM - 10PM',
            'website' : 'www.MangoliaCafe.com',
            })

    def test_restaurant_get_dict_3(self):
        self.assertEqual(Tests.r3.getDict(), {'name' : "Big Bite",
            'id' : Tests.r3.id,
            'reservation_required' : False,
            'reservation_avail' : False,
            'has_waiter' : True,
            'phone_number' : '1234445555',
            'description' : 'Amazing pizza',
            'zip_code' : '78705',
            'address' : '523 w 5th St',
            'delivery' : False,
            'take_out' : True,
            'pet_friendly' : True,
            'dollar_avg_rating' : 7,
            'dollar_num_rating' : 7,
            'dollar_sum_rating' : 49,
            'star_avg_rating' : 2,
            'star_num_rating' : 2,
            'star_sum_rating' : 4,
            'cuisine_id' : Tests.c1.id,
            'mon_hours' : '9AM - 10PM',
            'tue_hours' : '9AM - 10PM',
            'wed_hours' : '9AM - 10PM',
            'thu_hours' : '9AM - 10PM',
            'fri_hours' : '9AM - 10PM',
            'sat_hours' : '9AM - 10PM',
            'sun_hours' : '9AM - 10PM',
            'website' : 'www.BigBite.com'
            })

    # ----------------
    # customer get_dict
    # ----------------
    def test_customer_get_dict_1(self):
        self.assertEqual(Tests.cu1.getDict(), {'id' : Tests.cu1.id,"name": "Bobby", 'description' : "cool"})

    def test_customer_get_dict_2(self):
        self.assertEqual(Tests.cu2.getDict(), {'id' : Tests.cu2.id,"name": "Sam", 'description' : "ok"})

    def test_customer_get_dict_3(self):
        self.assertEqual(Tests.cu3.getDict(), {'id' : Tests.cu3.id,"name": "Jake", 'description' : "nice"})

    # --------------------
    # generic dish get_dict
    # --------------------
    def test_generic_dish_get_dict_1(self):
        self.assertEqual(Tests.gd1.getDict(), {'id' : Tests.gd1.id, "name":"Hamburger", 'cuisine_id' : Tests.c3.id})

    def test_generic_dish_get_dict_2(self):
        self.assertEqual(Tests.gd2.getDict(), {'id' : Tests.gd2.id, "name":"Pizza", 'cuisine_id' : Tests.c1.id})

    def test_generic_dish_get_dict_3(self):
        self.assertEqual(Tests.gd3.getDict(), {'id' : Tests.gd3.id, "name":"Sushi", 'cuisine_id' : Tests.c3.id})

    # ------------
    # dish get_dict
    # ------------
    def test_dish_get_dict_1(self):
        self.assertEqual(Tests.d1.getDict(),{'name' : 'Trifecta Pizza',
            'id' : Tests.d1.id,
            'star_avg_rating' : 4,
            'star_num_ratings' : 4,
            'star_sum_ratings' : 16,
            'dollar_avg_rating' : 3 ,
            'dollar_num_ratings' : 3,
            'dollar_sum_ratings' : 9,
            'vegetarian' : False,
            'vegan' : False,
            'kosher' : False,
            'halal' : False,
            'nut_allergy' : False,
            'restaurant_id' : Tests.r3.id,
            'generic_dish_id' : Tests.gd2.id,
            'cuisine_id' : Tests.c1.id,
            'description' : 'A trifecta of 3 meats including bacon'})

    def test_dish_get_dict_2(self):
        self.assertEqual(Tests.d2.getDict(),{'name' : 'Bacon Cheezburger',
        'id' : Tests.d2.id,
        'star_avg_rating' : 5,
        'star_num_ratings' : 5,
        'star_sum_ratings' : 25,
        'dollar_avg_rating' : 2 ,
        'dollar_num_ratings' : 5,
        'dollar_sum_ratings' : 10,
        'vegetarian' : False,
        'vegan' : False,
        'kosher' : False,
        'halal' : False,
        'nut_allergy' : False,
        'restaurant_id' : Tests.r1.id,
        'generic_dish_id' : Tests.gd1.id,
        'cuisine_id' : Tests.c1.id,
        'description' : 'Bacon with some cheezburger on it' })

    def test_dish_get_dict_3(self):
        self.assertEqual(Tests.d3.getDict(),{'name' : 'White Roll',
        'id' : Tests.d3.id,
        'star_avg_rating' : 3,
        'star_num_ratings' : 7,
        'star_sum_ratings' : 21,
        'dollar_avg_rating' : 2 ,
        'dollar_num_ratings' : 7,
        'dollar_sum_ratings' : 14,
        'vegetarian' : False,
        'vegan' : False,
        'kosher' : False,
        'halal' : False,
        'nut_allergy' : False,
        'restaurant_id' : Tests.r2.id,
        'generic_dish_id' : Tests.gd3.id,
        'cuisine_id' : Tests.c1.id,
        'description' : 'Prime sushi'})

    # -------------------------
    # restaurant review get_dict
    # -------------------------
    def test_restaurant_review_get_dict_1(self):
        self.assertEqual(Tests.rr1.getDict(), {'star_rating' : 1,
            'id' : Tests.rr1.id,
            'dollar_rating' : 5,
            'review_comment' : 'The food here stinks',
            'customer_id' : Tests.cu1.id,
            'restaurant_id' : Tests.r1.id
            })

    def test_restaurant_review_get_dict_2(self):
        self.assertEqual(Tests.rr2.getDict(), {
            'id' : Tests.rr2.id,
            'star_rating' : 5,
            'dollar_rating' : 1,
            'review_comment' : 'The food here da bomb dot com.',
            'customer_id' : Tests.cu2.id,
            'restaurant_id' : Tests.r2.id,
            })

    def test_restaurant_review_get_dict_3(self):
        self.assertEqual(Tests.rr3.getDict(), {
            'id' : Tests.rr3.id,
            'star_rating' : 3,
            'dollar_rating' : 3,
            'review_comment' : 'The food here is alright.',
            'customer_id' : Tests.cu3.id,
            'restaurant_id' : Tests.r3.id
            })

    # -------------------
    # dish review get_dict
    # -------------------
    def test_dish_review_get_dict_1(self):
        self.assertEqual(Tests.dr1.getDict(), {
            'id' : Tests.dr1.id,
            'star_rating' : 2,
            'dollar_rating' : 4,
            'review_comment' : 'Meh.',
            'customer_id' : Tests.cu1.id ,
            'dish_id' : Tests.d1.id
            })

    def test_dish_review_get_dict_2(self):
        self.assertEqual(Tests.dr2.getDict(), {
            'id' : Tests.dr2.id,
            'star_rating' : 5,
            'dollar_rating' : 2,
            'review_comment' : 'I love bacon! I love this burger!',
            'customer_id' : Tests.cu2.id ,
            'dish_id' : Tests.d2.id
            })

    def test_dish_review_get_dict_3(self):
        self.assertEqual(Tests.dr3.getDict(), {
            'id' : Tests.dr3.id,
            'star_rating' : 3,
            'dollar_rating' : 4,
            'review_comment' : 'Its ok but its a little expensive.',
            'customer_id' : Tests.cu3.id ,
            'dish_id' : Tests.d3.id
            })

    def model_instances():
        c1 = Cuisine.objects.create(name = "Ital")  # gets set to Italian soon after
        c2 = Cuisine.objects.create(name = "Mexi")  # gets set to Meixcan soon after
        c3 = Cuisine.objects.create(name = "Amer") # gets set to American soon after

        r1 = Restaurant.objects.create(
        name = "Kerbey Lane",
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
        star_sum_rating = 25,
        cuisine = c3,
        mon_hours = '11AM - 9PM',
        tue_hours = '11AM - 9PM',
        wed_hours = '11AM - 9PM',
        thu_hours = '11AM - 9PM',
        fri_hours = '11AM - 9PM',
        sat_hours = '11AM - 9PM',
        sun_hours = '11AM - 9PM',
        website = 'www.kerbey.com',
        )

        r2 = Restaurant.objects.create(
        name = "Magnolia",
        reservation_required = True,
        reservation_avail = False,
        has_waiter = False,
        phone_number = '5554445555',
        description = 'Amazing breakfast',
        zip_code = '78705',
        address = '555 w 5th St',
        delivery = False,
        take_out = True,
        pet_friendly = False,
        dollar_avg_rating = 6,
        dollar_num_rating = 6,
        dollar_sum_rating = 36,
        star_avg_rating = 4,
        star_num_rating = 4,
        star_sum_rating = 16,
        cuisine = c3,
        mon_hours = '9AM - 10PM',
        tue_hours = '9AM - 10PM',
        wed_hours = '9AM - 10PM',
        thu_hours = '9AM - 10PM',
        fri_hours = '9AM - 10PM',
        sat_hours = '9AM - 10PM',
        sun_hours = '9AM - 10PM',
        website = 'www.MangoliaCafe.com',
        )


        r3 = Restaurant.objects.create(
        name = "Big Bite",
        reservation_required = False,
        reservation_avail = False,
        has_waiter = True,
        phone_number = '1234445555',
        description = 'Amazing pizza',
        zip_code = '78705',
        address = '523 w 5th St',
        delivery = False,
        take_out = True,
        pet_friendly = True,
        dollar_avg_rating = 7,
        dollar_num_rating = 7,
        dollar_sum_rating = 49,
        star_avg_rating = 2,
        star_num_rating = 2,
        star_sum_rating = 4,
        cuisine = c1,
        mon_hours = '9AM - 10PM',
        tue_hours = '9AM - 10PM',
        wed_hours = '9AM - 10PM',
        thu_hours = '9AM - 10PM',
        fri_hours = '9AM - 10PM',
        sat_hours = '9AM - 10PM',
        sun_hours = '9AM - 10PM',
        website = 'www.BigBite.com'
        )

        cu1 = Customer.objects.create(name = "Bobby", description = "cool")
        cu2 = Customer.objects.create(name = "Sam", description = "ok")
        cu3 = Customer.objects.create(name = "Jake", description = "nice")
        gd1 = GenericDish.objects.create(name = "Hamburger", cuisine = c3)
        gd2 = GenericDish.objects.create(name = "Pizza", cuisine = c1)
        gd3 = GenericDish.objects.create(name = "Sushi", cuisine = c3)

        d1 = Dish.objects.create(
        name = 'Trifecta Pizza',
        star_avg_rating = 4,
        star_num_ratings = 4,
        star_sum_ratings = 16,
        dollar_avg_rating = 3 ,
        dollar_num_ratings = 3,
        dollar_sum_ratings = 9,
        vegetarian = False,
        vegan = False,
        kosher = False,
        halal = False,
        nut_allergy = False,
        restaurant = r3,
        generic_dish = gd2,
        cuisine = c1,
        description = 'A trifecta of 3 meats'
        )

        d2 = Dish.objects.create(
        name = 'Bacon Cheezburger',
        star_avg_rating = 5,
        star_num_ratings = 5,
        star_sum_ratings = 25,
        dollar_avg_rating = 2 ,
        dollar_num_ratings = 5,
        dollar_sum_ratings = 10,
        vegetarian = False,
        vegan = False,
        kosher = False,
        halal = False,
        nut_allergy = False,
        restaurant = r1,
        generic_dish = gd1,
        cuisine = c2,
        description = 'Bacon with some cheezburger on it'
        )

        d3 = Dish.objects.create(
        name = 'White Roll',
        star_avg_rating = 3,
        star_num_ratings = 7,
        star_sum_ratings = 21,
        dollar_avg_rating = 2 ,
        dollar_num_ratings = 7,
        dollar_sum_ratings = 14,
        vegetarian = False,
        vegan = False,
        kosher = False,
        halal = False,
        nut_allergy = False,
        restaurant = r2,
        generic_dish = gd3,
        cuisine = c1,
        description = 'Prime sushi'
        )

        rr1 = RestaurantReview.objects.create(
        star_rating = 1,
        dollar_rating = 5,
        review_comment = 'The food here stinks',
        customer = cu1,
        restaurant = r1,
        )

        rr2 = RestaurantReview.objects.create(
        star_rating = 5,
        dollar_rating = 1,
        review_comment = 'The food here da bomb dot com.',
        customer = cu2,
        restaurant = r2,
        )

        rr3 = RestaurantReview.objects.create(
        star_rating = 3,
        dollar_rating = 3,
        review_comment = 'The food here is alright.',
        customer = cu3,
        restaurant = r3,
        )

        dr1 = DishReview.objects.create(
        star_rating = 2,
        dollar_rating = 4,
        review_comment = 'Meh.',
        customer = cu1 ,
        dish = d1
        )

        dr2 = DishReview.objects.create(
        star_rating = 5,
        dollar_rating = 2,
        review_comment = 'I love bacon! I love this burger!',
        customer = cu2,
        dish = d2
        )

        dr3 = DishReview.objects.create(
        star_rating = 3,
        dollar_rating = 4,
        review_comment = 'Its ok but its a little expensive.',
        customer = cu3,
        dish = d3,
        )

        retDict = {'d1' : d1,
                  'd2' : d2,
                  'd3' : d3,
                  'r1' : r1,
                  'r2' : r2,
                  'r3' : r3,
                  'c1' : c1,
                  'c2' : c2,
                  'c3' : c3,
                  'cu1' : cu1,
                  'cu2' : cu2,
                  'cu3' : cu3,
                  'gd1' : gd1,
                  'gd2' : gd2,
                  'gd3' : gd3,
                  'rr1' : rr1,
                  'rr2' : rr2,
                  'rr3' : rr3,
                  'dr1' : dr1,
                  'dr2' : dr2,
                  'dr3' : dr3,
                  }
        return retDict

    def test_dish_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)['Dishes']

        dish_id = jresponse[0]['id']
        dish = Dish.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse[0]);

    def test_dish_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)['Dishes']

        dish_id = jresponse[1]['id']
        dish = Dish.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse[1]);

    def test_dish_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)['Dishes']

        dish_id = jresponse[2]['id']
        dish = Dish.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse[2]);

    def test_adish_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('adishjson', args=[Dish.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        dish_id = jresponse['id']
        dish = Dish.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse);

    def test_adish_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('adishjson', args=[Dish.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        dish_id = jresponse['id']
        dish = Dish.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse);

    def test_adish_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('adishjson', args=[Dish.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        dish_id = jresponse['id']
        dish = Dish.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse);

    def test_adish_json_4(self):
        Tests.model_instances()
        dishes = Dish.objects.all()
        response = self.client.get(reverse('adishjson', args=[len(dishes), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No dish found."}, jresponse);

    def test_dishesrevsjson_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesrevsjson', args=[DishReview.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)['Dish Reviews']

        dish_id = jresponse[0]['id']
        dish = DishReview.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse[0]);

    def test_dishesrevsjson_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesrevsjson', args=[DishReview.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)['Dish Reviews']

        dish_id = jresponse[0]['id']
        dish = DishReview.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse[0]);

    def test_dishesrevsjson_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesrevsjson', args=[DishReview.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)['Dish Reviews']

        dish_id = jresponse[0]['id']
        dish = DishReview.objects.get(pk = dish_id)

        self.assertEqual(dish.getDict(), jresponse[0]);

    def test_dishesrevsjson_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishesrevsjson', args=[len(Dish.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No dish reviews found."}, jresponse);

    def test_rest_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('restsjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse[0]['id']
        restaurant = Restaurant.objects.get(pk = restaurant_id)

        self.assertEqual(restaurant.getDict(), jresponse[0]);

    def test_rest_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('restsjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse[1]['id']
        restaurant = Restaurant.objects.get(pk = restaurant_id)

        self.assertEqual(restaurant.getDict(), jresponse[1]);

    def test_rest_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('restsjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse[2]['id']
        restaurant = Restaurant.objects.get(pk = restaurant_id)

        self.assertEqual(restaurant.getDict(), jresponse[2]);

    def test_arest_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('arestjson', args=[Restaurant.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['id']
        restaurant = Restaurant.objects.get(pk = restaurant_id)

        self.assertEqual(restaurant.getDict(), jresponse);

    def test_arest_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('arestjson', args=[Restaurant.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['id']
        restaurant = Restaurant.objects.get(pk = restaurant_id)

        self.assertEqual(restaurant.getDict(), jresponse);

    def test_arest_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('arestjson', args=[Restaurant.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['id']
        restaurant = Restaurant.objects.get(pk = restaurant_id)

        self.assertEqual(restaurant.getDict(), jresponse);

    def test_arest_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('arestjson', args=[len(Restaurant.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No restaurant found."}, jresponse);

    def test_restdish_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('restdishjson', args=[Restaurant.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['Restaurant Dishes'][0]['restaurant_id']
        dish = Dish.objects.get(restaurant_id = restaurant_id)

        self.assertEqual(dish.getDict(), jresponse['Restaurant Dishes'][0]);

    def test_restdish_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('restdishjson', args=[Restaurant.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['Restaurant Dishes'][0]['restaurant_id']
        dish = Dish.objects.get(restaurant_id = restaurant_id)

        self.assertEqual(dish.getDict(), jresponse['Restaurant Dishes'][0]);

    def test_restdish_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('restdishjson', args=[Restaurant.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['Restaurant Dishes'][0]['restaurant_id']
        dish = Dish.objects.get(restaurant_id = restaurant_id)

        self.assertEqual(dish.getDict(), jresponse['Restaurant Dishes'][0]);

    def test_restdish_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('restdishjson', args=[len(Restaurant.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No restaurant dishes found."}, jresponse);

    def test_restrev_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevjson', args=[Restaurant.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['Restaurant Reviews'][0]['restaurant_id']
        review = RestaurantReview.objects.get(restaurant_id = restaurant_id)

        self.assertEqual(review.getDict(), jresponse['Restaurant Reviews'][0]);

    def test_restrev_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevjson', args=[Restaurant.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['Restaurant Reviews'][0]['restaurant_id']
        review = RestaurantReview.objects.get(restaurant_id = restaurant_id)

        self.assertEqual(review.getDict(), jresponse['Restaurant Reviews'][0]);

    def test_restrev_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevjson', args=[Restaurant.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        restaurant_id = jresponse['Restaurant Reviews'][0]['restaurant_id']
        review = RestaurantReview.objects.get(restaurant_id = restaurant_id)

        self.assertEqual(review.getDict(), jresponse['Restaurant Reviews'][0]);

    def test_restrev_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevjson', args=[len(Restaurant.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No restaurant reviews found."}, jresponse);

    def test_custs_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('custsjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customers'][0]['id']
        customer = Customer.objects.get(pk = customer_id)

        self.assertEqual(customer.getDict(), jresponse['Customers'][0]);

    def test_custs_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('custsjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customers'][1]['id']
        customer = Customer.objects.get(pk = customer_id)

        self.assertEqual(customer.getDict(), jresponse['Customers'][1]);

    def test_custs_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('custsjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customers'][2]['id']
        customer = Customer.objects.get(pk = customer_id)

        self.assertEqual(customer.getDict(), jresponse['Customers'][2]);

    def test_acust_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('acustjson', args=[Customer.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['id']
        customer = Customer.objects.get(pk = customer_id)

        self.assertEqual(customer.getDict(), jresponse);

    def test_acust_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('acustjson', args=[Customer.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['id']
        customer = Customer.objects.get(pk = customer_id)

        self.assertEqual(customer.getDict(), jresponse);

    def test_acust_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('acustjson', args=[Customer.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['id']
        customer = Customer.objects.get(pk = customer_id)

        self.assertEqual(customer.getDict(), jresponse);

    def test_acust_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('acustjson', args=[len(Customer.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No customer found."}, jresponse);

    def test_restrevs_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevsjson', args=[Customer.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customer Restaurant Reviews'][0]['customer_id']
        rest_review = RestaurantReview.objects.get(customer_id = customer_id)

        self.assertEqual(rest_review.getDict(), jresponse['Customer Restaurant Reviews'][0]);

    def test_restrevs_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevsjson', args=[Customer.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customer Restaurant Reviews'][0]['customer_id']
        rest_review = RestaurantReview.objects.get(customer_id = customer_id)

        self.assertEqual(rest_review.getDict(), jresponse['Customer Restaurant Reviews'][0]);

    def test_restrevs_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevsjson', args=[Customer.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customer Restaurant Reviews'][0]['customer_id']
        rest_review = RestaurantReview.objects.get(customer_id = customer_id)

        self.assertEqual(rest_review.getDict(), jresponse['Customer Restaurant Reviews'][0]);

    def test_restrevs_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('restrevsjson', args=[len(Customer.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No customer restaurant reviews found."}, jresponse);

    def test_dishrevs_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishrevsjson', args=[Customer.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customer Dish Reviews'][0]['customer_id']
        dish_review = DishReview.objects.get(customer_id = customer_id)

        self.assertEqual(dish_review.getDict(), jresponse['Customer Dish Reviews'][0]);

    def test_dishrevs_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishrevsjson', args=[Customer.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customer Dish Reviews'][0]['customer_id']
        dish_review = DishReview.objects.get(customer_id = customer_id)

        self.assertEqual(dish_review.getDict(), jresponse['Customer Dish Reviews'][0]);

    def test_dishrevs_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishrevsjson', args=[Customer.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        customer_id = jresponse['Customer Dish Reviews'][0]['customer_id']
        dish_review = DishReview.objects.get(customer_id = customer_id)

        self.assertEqual(dish_review.getDict(), jresponse['Customer Dish Reviews'][0]);

    def test_dishrevs_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('dishrevsjson', args=[len(Customer.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No customer dish reviews found."}, jresponse);

    def test_gdishes_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('gdishesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_dish_id = jresponse['Generic Dishes'][0]['id']
        gen_dish = GenericDish.objects.get(pk = generic_dish_id)

        self.assertEqual(gen_dish.getDict(), jresponse['Generic Dishes'][0]);

    def test_gdishes_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('gdishesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_dish_id = jresponse['Generic Dishes'][1]['id']
        gen_dish = GenericDish.objects.get(pk = generic_dish_id)

        self.assertEqual(gen_dish.getDict(), jresponse['Generic Dishes'][1]);

    def test_gdishes_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('gdishesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_dish_id = jresponse['Generic Dishes'][2]['id']
        gen_dish = GenericDish.objects.get(pk = generic_dish_id)

        self.assertEqual(gen_dish.getDict(), jresponse['Generic Dishes'][2]);

    def test_agdish_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishjson', args=[GenericDish.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_dish_id = jresponse['id']
        gen_dish = GenericDish.objects.get(pk = generic_dish_id)

        self.assertEqual(gen_dish.getDict(), jresponse);

    def test_agdish_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishjson', args=[GenericDish.objects.all()[1].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_dish_id = jresponse['id']
        gen_dish = GenericDish.objects.get(pk = generic_dish_id)

        self.assertEqual(gen_dish.getDict(), jresponse);

    def test_agdish_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishjson', args=[GenericDish.objects.all()[2].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_dish_id = jresponse['id']
        gen_dish = GenericDish.objects.get(pk = generic_dish_id)

        self.assertEqual(gen_dish.getDict(), jresponse);

    def test_agdish_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishjson', args=[len(GenericDish.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No generic dish found."}, jresponse);

    def test_agdishdishes_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishdishesjson', args=[GenericDish.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_id = jresponse['Dishes'][0]['generic_dish_id']
        dish = Dish.objects.get(generic_dish_id = generic_id)

        self.assertEqual(dish.getDict(), jresponse['Dishes'][0]);

    def test_agdishdishes_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishdishesjson', args=[GenericDish.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_id = jresponse['Dishes'][0]['generic_dish_id']
        dish = Dish.objects.get(generic_dish_id = generic_id)

        self.assertEqual(dish.getDict(), jresponse['Dishes'][0]);

    def test_agdishdishes_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishdishesjson', args=[GenericDish.objects.all()[0].id, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)

        generic_id = jresponse['Dishes'][0]['generic_dish_id']
        dish = Dish.objects.get(generic_dish_id = generic_id)

        self.assertEqual(dish.getDict(), jresponse['Dishes'][0]);

    def test_agdishdishes_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('agdishdishesjson', args=[len(GenericDish.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No generic dish dishes found."}, jresponse);

    def test_cuisines_json_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('cuisinesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine_id = jresponse['Cuisines'][0]['id']
        cuisine = Cuisine.objects.get(pk = cuisine_id)
        self.assertEqual(cuisine.getDict(), jresponse['Cuisines'][0]);

    def test_cuisines_json_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('cuisinesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine_id = jresponse['Cuisines'][1]['id']
        cuisine = Cuisine.objects.get(pk = cuisine_id)
        self.assertEqual(cuisine.getDict(), jresponse['Cuisines'][1]);

    def test_cuisines_json_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('cuisinesjson', args=['json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine_id = jresponse['Cuisines'][2]['id']
        cuisine = Cuisine.objects.get(pk = cuisine_id)
        self.assertEqual(cuisine.getDict(), jresponse['Cuisines'][2]);

    def test_a_cuisine_json_1(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[0].id
        response = self.client.get(reverse('acuisinejson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        self.assertEqual(cuisine.getDict(), jresponse);

    def test_a_cuisine_json_2(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[1].id
        response = self.client.get(reverse('acuisinejson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        self.assertEqual(cuisine.getDict(), jresponse);

    def test_a_cuisine_json_3(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[2].id
        response = self.client.get(reverse('acuisinejson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        self.assertEqual(cuisine.getDict(), jresponse);

    def test_a_cuisine_json_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('acuisinejson', args=[len(Cuisine.objects.all()), 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No cuisine found."}, jresponse);

    def test_cuisines_dishes_json_1(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[0].id
        response = self.client.get(reverse('acuisinesdishesjson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        dishList = []
        for dish in cuisine.dish_set.all():
          dishList.append(dish.getDict())
        self.assertEqual(dishList, jresponse['Cuisine Dishes']);

    def test_cuisines_dishes_json_2(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[1].id
        response = self.client.get(reverse('acuisinesdishesjson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        dishList = []
        for dish in cuisine.dish_set.all():
          dishList.append(dish.getDict())
        self.assertEqual(dishList, jresponse['Cuisine Dishes']);

    def test_cuisines_dishes_json_3(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = len(cuisines)
        response = self.client.get(reverse('acuisinesdishesjson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No cuisine dishes found."}, jresponse);

    def test_cuisines_restaurants_json_1(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[0].id
        response = self.client.get(reverse('acuisinesrestsjson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        restList = []
        for rest in cuisine.restaurant_set.all():
          restList.append(rest.getDict())
        self.assertEqual(restList, jresponse['Cuisine Restaurants']);

    def test_cuisines_restaurants_json_2(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = cuisines[2].id
        response = self.client.get(reverse('acuisinesrestsjson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        cuisine = Cuisine.objects.get(pk = cid)
        restList = []
        for rest in cuisine.restaurant_set.all():
          restList.append(rest.getDict())
        self.assertEqual(restList, jresponse['Cuisine Restaurants']);

    def test_cuisines_restaurants_json_3(self):
        Tests.model_instances()
        cuisines = Cuisine.objects.all()
        cid = len(cuisines)
        response = self.client.get(reverse('acuisinesrestsjson', args=[cid, 'json']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual({"Error" : "No cuisine restaurants found."}, jresponse);

    def verify_search_result_string(self, string):
        pat = re.compile("(<strong>|</strong>)")
        matches = re.finditer(pat, string) 

        match = next(matches)
        self.assertEqual("<strong>", match.group())

        match = next(matches)
        self.assertEqual("</strong>", match.group())

        #for match in matches:
        while True:
            try:
                match = next(matches)
                self.assertEqual("<strong>", match.group())
            except StopIteration:
                break
            try:
                match = next(matches)
                self.assertEqual("</strong>", match.group())
            except StopIteration:
                self.assertTrue(False)


    def verify_search_results(self, searchResultDictList):
        for result in searchResultDictList:
            if result["modelType"] == "Dish":
                instance = Dish.objects.get(pk=result["id"])
                url = reverse('adishjson', args=[instance.id])
            elif result["modelType"] == "Restaurant":
                instance = Restaurant.objects.get(pk=result["id"])
                url = reverse('arestjson', args=[instance.id])
            else:
                self.assertTrue(False)

        self.assertEqual(instance.name, result["name"])
        self.assertEqual(url, result["url"])
        self.assertTrue(result["type"] == "and" or result["type"] == "or")
        Tests.verify_search_result_string(self, result["text"])
        
    
        return True


    def test_search_dish_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['blank']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual([], jresponse);

    def test_search_dish_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['pizza']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(2, len(jresponse))

    def test_search_dish_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['sushi']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(2, len(jresponse))

    def test_search_dish_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['bacon']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(2, len(jresponse))

    def test_search_dish_5(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['bacon burger']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(2, len(jresponse))

    def test_search_dish_5(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['bacon blank']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(1, len(jresponse))

    def test_search_rest_1(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['blank']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        self.assertEqual([], jresponse);

    def test_search_rest_2(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['magnolia']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(2, len(jresponse))

    def test_search_rest_3(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['kerbey']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(2, len(jresponse))

    def test_search_rest_4(self):
        Tests.model_instances()
        response = self.client.get(reverse('search', args=['kerbey breakfast']))
        b = str(response.content)[2:-1]
        jresponse = json.loads(b)
        Tests.verify_search_results(self, jresponse)
        self.assertEqual(1, len(jresponse))
