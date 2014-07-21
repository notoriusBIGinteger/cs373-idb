from rest_framework import serializers
from ourapp.models import *

class RestaurantSerializer(serializers.Serializer):
    id = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(max_length=100)
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
    cost = serializers.CharField(max_length=5)
    website = serializers.CharField(max_length=50)
    cuisine = serializers.CharField(max_length=50)

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
    rating = serializers.CharField(max_length=1)
    num_ratings = serializers.CharField(max_length=10)
    sum_of_ratings = serializers.CharField(max_length=10)
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
            instance.rating = attrs.get('Rating', instance.rating)
            instance.num_ratings = attrs.get('Number of Ratings', instance.num_ratings)
            instance.sum_of_ratings = attrs.get('Sum Of Ratings', instance.sum_of_ratings)
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
        return GenericDish(**attrs)