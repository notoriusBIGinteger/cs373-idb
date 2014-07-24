from rest_framework import serializers
from ourapp.models import *

class RestaurantSerializer(serializers.Serializer):
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=30)
    reservation_required = serializers.BooleanField(required=False)
    reservation_avail = serializers.BooleanField(required=False)
    has_waiter = serializers.BooleanField(required=False)
    phone_number = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=200)
    zip_code = serializers.CharField(max_length=5)
    address = serializers.CharField(max_length=50)
    delivery = serializers.BooleanField(required=False)
    take_out = serializers.BooleanField(required=False)
    pet_friendly = serializers.BooleanField(required=False)
    dollar_avg_rating = serializers.FloatField()
    dollar_num_rating = serializers.IntegerField()
    dollar_sum_rating = serializers.IntegerField()
    star_avg_rating = serializers.FloatField()
    star_num_rating = serializers.IntegerField()
    star_sum_rating = serializers.IntegerField()
    website = serializers.URLField()
    cuisine_id = serializers.IntegerField()
    mon_hours = serializers.CharField(max_length=200)
    tue_hours = serializers.CharField(max_length=200)
    wed_hours = serializers.CharField(max_length=200)
    thu_hours = serializers.CharField(max_length=200)
    fri_hours = serializers.CharField(max_length=200)
    sat_hours = serializers.CharField(max_length=200)
    sun_hours = serializers.CharField(max_length=200)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Restaurant instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('Name', instance.name)
            instance.reservation_required = attrs.get('Reservation Required', instance.reservation_required)
            instance.reservation_avail = attrs.get('Reservations Available', instance.reservation_avail )
            instance.has_waiter = attrs.get('Waiter Service', instance.has_waiter)
            instance.phone_number = attrs.get('Phone Number', instance.phone_number )
            instance.description = attrs.get('Description', instance.description)
            instance.zip_code = attrs.get('Zip Code', instance.zip_code)
            instance.address = attrs.get('Address', instance.address)
            instance.delivery = attrs.get('Delivery Available', instance.delivery)
            instance.take_out = attrs.get('Take-out Available', instance.take_out)
            instance.pet_friendly = attrs.get('Pet Friendly', instance.pet_friendly)
            instance.dollar_avg_rating = attrs.get('Avg. of Dollar Ratings', instance.dollar_avg_rating)
            instance.dollar_num_rating = attrs.get('Avg. of Dollar Ratings', instance.dollar_num_rating)
            instance.dollar_sum_rating = attrs.get('Avg. of Dollar Ratings', instance.dollar_sum_rating)
            instance.star_avg_rating = attrs.get('Avg. of Ratings', instance.star_avg_rating)
            instance.star_num_rating = attrs.get('Number of Ratings', instance.star_num_rating)
            instance.star_sum_rating = attrs.get('Sum of Ratings', instance.star_sum_rating)
            instance.website = attrs.get('Website', instance.website)
            instance.cuisine_id = attrs.get('Cuisine', instance.cuisine_id)
            instance.mon_hours = attrs.get('Monday Hours', instance.mon_hours)
            instance.tue_hours = attrs.get('Tuesday Hours', instance.tue_hours)
            instance.wed_hours = attrs.get('Wednesday Hours', instance.wed_hours)
            instance.thu_hours = attrs.get('Thursday Hours', instance.thu_hours)
            instance.fri_hours = attrs.get('Friday Hours', instance.fri_hours)
            instance.sat_hours = attrs.get('Saturday Hours', instance.sat_hours)
            instance.sun_hours = attrs.get('Sunday Hours', instance.sun_hours)
            return instance

        # Create new instance
        return Restaurant(**attrs)

class RestaurantReviewsSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    star_rating = serializers.IntegerField()
    dollar_rating = serializers.IntegerField()
    review_comment = serializers.CharField(max_length=250)
    customer_id = serializers.IntegerField()
    restaurant_id = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Restaurant Review instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.star_rating = attrs.get('Star Rating', instance.star_rating)
            instance.dollar_rating = attrs.get('Dollar Rating', instance.dollar_rating)
            instance.review_comment = attrs.get('Review', instance.review_comment)
            instance.customer_id = attrs.get('Customer', instance.customer_id )
            instance.restaurant_id = attrs.get('Restaurant', instance.restaurant_id)

            return instance

        # Create new instance
        return RestaurantReview(**attrs)

class DishesSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=40)
    star_avg_rating = serializers.FloatField()
    star_num_ratings = serializers.IntegerField()
    star_sum_ratings = serializers.IntegerField()
    dollar_avg_rating = serializers.FloatField()
    dollar_num_ratings = serializers.IntegerField()
    dollar_sum_ratings = serializers.IntegerField()
    vegetarian = serializers.BooleanField(required=False)
    vegan = serializers.BooleanField(required=False)
    kosher = serializers.BooleanField(required=False)
    halal = serializers.BooleanField(required=False)
    nut_allergy = serializers.BooleanField(required=False)
    restaurant_id = serializers.IntegerField()
    generic_dish_id = serializers.IntegerField()
    cuisine_id = serializers.IntegerField()
    description = serializers.CharField(max_length=300)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Dish instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('Name', instance.name)
            instance.star_avg_rating = attrs.get('Star Avg. Rating', instance.star_avg_rating)
            instance.star_num_ratings = attrs.get('Num. Star Ratings', instance.star_num_ratings)
            instance.star_sum_ratings = attrs.get('Sum Star Ratings', instance.star_sum_ratings)
            instance.dollar_avg_rating = attrs.get('Dollar Avg. Ratings', instance.dollar_avg_rating)
            instance.dollar_num_ratings = attrs.get('Num Dollar Ratings', instance.dollar_num_ratings)
            instance.dollar_sum_ratings = attrs.get('Sum Dollar Ratings', instance.dollar_sum_ratings)
            instance.vegetarian = attrs.get('Vegetarian', instance.vegetarian)
            instance.vegan = attrs.get('Vegan', instance.vegan)
            instance.kosher = attrs.get('Kosher', instance.kosher)
            instance.halal = attrs.get('Halal', instance.halal)
            instance.nut_allergy = attrs.get('Nut Allergy', instance.nut_allergy)
            instance.restaurant_id = attrs.get('Restaurant', instance.restaurant_id)
            instance.generic_dish_id = attrs.get('Generic Dish', instance.generic_dish_id)
            instance.cuisine_id = attrs.get('Cuisine', instance.cuisine_id)
            instance.description = attrs.get('Description', instance.description)
            return instance

        # Create new instance
        return Dish(**attrs)

class DishReviewsSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    star_rating = serializers.IntegerField()
    dollar_rating = serializers.IntegerField()
    review_comment = serializers.CharField(max_length=250)
    customer_id = serializers.IntegerField()
    dish_id = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Restaurant Review instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.star_rating = attrs.get('Star Rating', instance.star_rating)
            instance.dollar_rating = attrs.get('Dollar Rating', instance.dollar_rating)
            instance.review_comment = attrs.get('Review', instance.review_comment)
            instance.customer_id = attrs.get('Customer', instance.customer_id)
            instance.dish_id = attrs.get('Dish', instance.dish_id)

            return instance

        # Create new instance
        return DishReview(**attrs)

class CustomerSerializer(serializers.Serializer):
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=35)
    description = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Customer instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('Name', instance.name)
            instance.description = attrs.get('Description', instance.description)
            return instance

        # Create new instance
        return Customer(**attrs)

class GenericDishSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=30)
    cuisine_id = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Generic Dish instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('Name', instance.name)
            instance.cuisine_id = attrs.get('Cuisine', instance.cuisine_id)

            return instance

        # Create new instance
        return GenericDish(**attrs)

class CuisineSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=30)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Generic Dish instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('Name', instance.name)

            return instance

        # Create new instance
        return Cuisine(**attrs)