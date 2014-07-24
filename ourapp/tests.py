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

    cu1 = Customer(name = "Bobby")
    cu2 = Customer(name = "Sam")
    cu3 = Customer(name = "Jake")
    gd1 = GenericDish(name = "Hamburger")
    gd2 = GenericDish(name = "Pizza")
    gd3 = GenericDish(name = "Sushi")

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
    description = 'A trifecta of 3 meats' 
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
    review_comment = "It's ok but it's a little expensive.", 
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
        self.assertEqual(Tests.cu1.get_all(), {"name": "Bobby"})

    def test_customer_get_all_2(self):
        self.assertEqual(Tests.cu2.get_all(), {"name": "Sam"})

    def test_customer_get_all_3(self):
        self.assertEqual(Tests.cu3.get_all(), {"name": "Jake"})

    # --------------------
    # generic dish get_all
    # --------------------
    def test_generic_dish_get_all_1(self):
        self.assertEqual(Tests.gd1.get_all(), {"name":"Hamburger"})

    def test_generic_dish_get_all_2(self):
        self.assertEqual(Tests.gd2.get_all(), {"name":"Pizza"})

    def test_generic_dish_get_all_3(self):
        self.assertEqual(Tests.gd3.get_all(), {"name":"Sushi"})

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
            'description' : 'A trifecta of 3 meats'})

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
            'review_comment' : "It's ok but it's a little expensive.",
            'customer' : Tests.cu3 ,
            'dish' : Tests.d3
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

        cu1 = Customer.objects.create(name = "Bobby")
        cu2 = Customer.objects.create(name = "Sam")
        cu3 = Customer.objects.create(name = "Jake")
        gd1 = GenericDish.objects.create(name = "Hamburger")
        gd2 = GenericDish.objects.create(name = "Pizza")
        gd3 = GenericDish.objects.create(name = "Sushi")

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
        description = 'A trifecta of 3 meats' 
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
        review_comment = "It's ok but it's a little expensive.", 
        customer = cu3,
        dish = d3,
        )
        
        retDict = {'d1' : d1}
        return retDict
        
        
    def test_table(self):
        modelsDict = Tests.model_instances()
        response = self.client.get(reverse('restsjson', args=['json']))
        b = str(response.content)[2:-1]#.replace("\\n", "")
        print('b=',b,'=b',sep='')
        json.loads(b)

    def test_table_2(self):
        response = self.client.get(reverse('restsjson', args=['json']))
        b = str(response.content)[2:-1]#.replace("\\n", "")
        print('b=',b,'=b',sep='')
        json.loads(b)
         

