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
    cost = serializers.IntegerField()
    star_avg_rating = serializers.FloatField()
    star_num_rating = serializers.IntegerField()
    star_sum_rating = serializers.IntegerField()
    website = serializers.URLField()
    cuisine_id = serializers.Field()

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
            instance.cost = attrs.get('Cost', instance.cost)
            instance.star_avg_rating = attrs.get('Avg. of Ratings', instance.star_avg_rating)
            instance.star_num_rating = attrs.get('Number of Ratings', instance.star_num_rating)
            instance.star_sum_rating = attrs.get('Sum of Ratings', instance.star_sum_rating)
            instance.website = attrs.get('Website', instance.website)
            instance.cuisine = attrs.get('Cuisine', instance.cuisine)
            return instance

        # Create new instance
        return Restaurant(**attrs)

class RestaurantReviewsSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    rating = serializers.CharField(max_length=1)
    review_comment = serializers.CharField(max_length=500)
    customer_id = serializers.CharField(max_length=5)
    restaurant_id = serializers.CharField(max_length=5)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Restaurant Review instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.rating = attrs.get('Rating', instance.name)
            instance.review_comment = attrs.get('Review', instance.reservation_required)
            instance.customer_id = attrs.get('Customer', instance.reservation_avail )
            instance.restaurant_id = attrs.get('Restaurant', instance.has_waiter)

            return instance

        # Create new instance
        return RestaurantReview(**attrs)

class DishesSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=100)
    star_avg_rating = serializers.CharField(max_length=10)
    star_num_ratings = serializers.CharField(max_length=10)
    star_sum_ratings = serializers.CharField(max_length=10)
    dollar_avg_rating = serializers.CharField(max_length=10)
    dollar_num_ratings = serializers.CharField(max_length=10)
    dollar_sum_ratings = serializers.CharField(max_length=10)
    vegetarian = serializers.BooleanField(required=False)
    vegan = serializers.BooleanField(required=False)
    kosher = serializers.BooleanField(required=False)
    halal = serializers.BooleanField(required=False)
    nut_allergy = serializers.BooleanField(required=False)
    cost = serializers.BooleanField(required=False)
    restaurant_id = serializers.CharField(max_length=5)
    generic_dish_id = serializers.CharField(max_length=5)

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
            instance.cost = attrs.get('Cost', instance.cost)
            instance.restaurant_id = attrs.get('Restaurant', instance.restaurant_id)
            instance.generic_dish_id = attrs.get('Generic Dish', instance.generic_dish_id )
            return instance

        # Create new instance
        return Dish(**attrs)

class CustomerSerializer(serializers.Serializer):
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=100)

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
            return instance

        # Create new instance
        return Customer(**attrs)

class DishReviewsSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    rating = serializers.CharField(max_length=1)
    review_comment = serializers.CharField(max_length=500)
    customer_id = serializers.CharField(max_length=5)
    dish_id = serializers.CharField(max_length=5)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new Restaurant Review instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.rating = attrs.get('Rating', instance.name)
            instance.review_comment = attrs.get('Review', instance.reservation_required)
            instance.customer_id = attrs.get('Customer', instance.reservation_avail )
            instance.dish_id = attrs.get('Dish', instance.has_waiter)

            return instance

        # Create new instance
        return DishReview(**attrs)

class GenericDishSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=100)
    cuisine_id = serializers.CharField(max_length=5)

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
            instance.cuisine_id = attrs.get('Cuisine', instance.reservation_required)

            return instance

        # Create new instance
        return GenericDish(**attrs)

class CuisineSerializer(serializers.Serializer) :
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=100)

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