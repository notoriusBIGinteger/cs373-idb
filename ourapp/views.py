from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from collections import OrderedDict

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ourapp.models import *
from ourapp.serializers import *

def dish_temp(request):
    dish_result = Dish.objects.order_by('name')
    #context = {'dish_result':dish_result}

    d_serializer = DishesSerializer(dish_result, many=True)

    return render_to_response('ourapp/dish_temp.html', {'dish_result' : d_serializer.data})

    #return render(request,'ourapp/dish_temp.html',context)

def splash(request):
    context = {}
    return render(request, 'ourapp/splash.html', context)

def temp(request):
  context = {}
  return render(request, 'ourapp/master.html', context)

def rest(request):
  context = {}
  return render(request, 'ourapp/rest.html', context)

def nate_test(request):
  customers =  Customer.objects.all()
  serializer = CustomerSerializer(customers, many=True)

  d = {"Customers" : serializer.data}

  return render_to_response('ourapp/nathan_test.html', {'items' : d['Customers']})

# Create your views here.
def customer(request, customerID):
  customerIDInt = int(customerID) #make int so 1, 01, or 001, all work.
  context = {}
  if customerIDInt == 1:
    return render(request, 'ourapp/omar-lalani.html', context)
  elif customerIDInt == 2:
    return render(request, 'ourapp/mike-wham.html', context)
  elif customerIDInt == 3:
    return render(request, 'ourapp/kevin-wheeler.html', context)
  else:
    raise Http404

def dish(request, dishID):
  dishIDInt = int(dishID) #make int so 1, 01, or 001, all work.
  context = {}
  if dishIDInt == 1:
    return render(request, 'ourapp/magnolia-cafe-alfredo-pasta.html', context)
  elif dishIDInt == 2:
    return render(request, 'ourapp/hyde-park-grill-ceasar-salad.html', context)
  elif dishIDInt == 3:
    return render(request, 'ourapp/hyde-park-bar-grill-blackened-fish-tacos.html', context)
  else:
    raise Http404

def restaurant(request, restaurantID):
  restaurantIDInt = int(restaurantID) #make int so 1, 01, or 001, all work.
  context = {}
  if restaurantIDInt == 1:
    return render(request, 'ourapp/kerbey-lane.html', context)
  elif restaurantIDInt == 2:
    return render(request, 'ourapp/magnolia-cafe.html', context)
  elif restaurantIDInt == 3:
    return render(request, 'ourapp/hyde-park-grill.html',context)
  else:
    raise Http404

def index(request):
  context = {}
  return render(request, 'ourapp/index.html', context)

class JSONResponse(HttpResponse) :
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data, renderer_context = {'indent' : 4})
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def restaurant_list(request, format=None):
    """
    List all Restaurants.
    """

    if request.method == 'GET':
        restaurants =  Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)

        if format is None :
            return render_to_response('ourapp/restaurant.html', {'restaurants_result': serializer.data })
        elif format.lower() == 'json' :
            restaurant_dictionary = {"Restaurants" : serializer.data}
            for restaurant in restaurant_dictionary['Restaurants'] :
                restaurant['restaurant_id'] = restaurant.pop('id')

            return JSONResponse(restaurant_dictionary)
        else :
            return JSONResponse({})

        #Nathan I (alex) commented the stuff under to see if my restaurant page worked
        #^Alex, I fixed the problem- pass in the dictionary. RestaurantSerializer is just a class I wrote.

        #for x in d['Restaurants'] :
        #    x['restaurant_id'] = x.pop('id')

        #return JSONResponse(d)

@csrf_exempt
def restaurant_detail(request, pk, format=None):
    """
    Retrieve a Restaurant.
    """
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        dish_results = Dish.objects.all().filter(restaurant = pk)
        customer_reviews = RestaurantReview.objects.all().filter(restaurant = pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Restaurant not found', status=404)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)

        serializer.data['restaurant_id'] = serializer.data.pop('id')

        if format is None :
            return render_to_response('ourapp/restaurant_attributes.html', { 'restaurant' : serializer.data, 'dish_results':dish_results,'customer_reviews':customer_reviews })
        elif format.lower() == 'json' :
            return JSONResponse(serializer.data)

@csrf_exempt
def restaurant_dishes(request, pk, format=None):
    """
    Retrieve a Restaurant's dishes.
    """
    try:
        restaurant_dishes = Dish.objects.all().filter(restaurant_id = pk)
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Restaurant not found', status=404)

    if request.method == 'GET':
        #serializer = DishesSerializer(restaurant_dishes, many=True)

        #for x in serializer.data :
        #    x['dish_id'] = x.pop('id')

        if format is None :
            return render_to_response('ourapp/restaurant_dishes.html', { 'restaurant_dishes' : restaurant_dishes,'restaurant':restaurant })
        #elif format.lower() == 'json' :
        #    return JSONResponse( { 'Restaurant Dishes' : serializer.data} )

@csrf_exempt
def restaurant_reviews(request, pk, format=None):
    """
    Retrieve a Restaurant's dishes.
    """
    try:
        customer_reviews = RestaurantReview.objects.all().filter(restaurant = pk)
        restaurant = Restaurant.objects.get(pk = pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Restaurant not found', status=404)

    if request.method == 'GET':
        serializer = RestaurantReviewsSerializer(customer_reviews, many=True)

        for y in serializer.data :
            y['review_id'] = y.pop('id')

        if format is None :
            return render_to_response('ourapp/restaurant_reviews.html', { 'customer_reviews' : customer_reviews, 'restaurant':restaurant })
            #return render_to_response('ourapp/restaurant_reviews.html', { 'customer_reviews': serializer.data})
        elif format.lower() == 'json' :
            return JSONResponse({ 'Restaurant Reviews' : serializer.data })

@csrf_exempt
def customer_list(request, format=None):
    """
    List all Customers.
    """
    if request.method == 'GET':
        customers =  Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        if format is None :
            return render_to_response('ourapp/customer.html', { 'customers_result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Customers' : serializer.data })

@csrf_exempt
def customer_detail(request, pk, format=None):
    """
    Retrieve a Customer.
    """
    try:
        customer = Customer.objects.get(pk=pk)
        dish_reviews = DishReview.objects.all().filter(customer = pk)
        restaurant_reviews = RestaurantReview.objects.all().filter(customer = pk)
    except Customer.DoesNotExist:
        return HttpResponse(content='Customer not found', status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)

        if format is None :
            return render_to_response('ourapp/customer_attributes.html', {'customer' : serializer.data, 'dish_reviews':dish_reviews,'restaurant_reviews':restaurant_reviews})
        elif format.lower() == 'json' :
            return JSONResponse(serializer.data)

@csrf_exempt
def customer_restaurant_reviews(request, pk, format=None):
    """
    Retrieve a Customer's reviews.
    """
    try:
        customer_r_reviews = RestaurantReview.objects.all().filter(customer_id = pk)
        customer = Customer.objects.get(pk=pk)
    except RestaurantReview.DoesNotExist:
        return HttpResponse(content='Customer not found', status=404)

    if request.method == 'GET':
        serializer = RestaurantReviewsSerializer(customer_r_reviews, many=True)

        if format is None :
            return render_to_response('ourapp/customer_restaurant_reviews.html', { 'customer_r_reviews' : customer_r_reviews, 'customer':customer})
        elif format.lower() == 'json' :
            return JSONResponse({ 'Customer Restaurant Reviews' : serializer.data })

@csrf_exempt
def customer_dish_reviews(request, pk, format=None):
    """
    Retrieve a Customer's reviews.
    """
    try:
        customer_d_reviews = DishReview.objects.all().filter(customer_id = pk)
        customer = Customer.objects.get(pk = pk)
    except DishReview.DoesNotExist:
        return HttpResponse(content='Customer not found', status=404)

    if request.method == 'GET':
        serializer = DishReviewsSerializer(customer_d_reviews, many=True)

        if format is None :
            return render_to_response('ourapp/customer_dish_reviews.html', { 'customer_d_reviews' : customer_d_reviews, 'customer':customer })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Customer Dish Reviews' : serializer.data })

@csrf_exempt
def dish_list(request, format=None):
    """
    List all Dishes.
    """
    if request.method == 'GET':
        dishes =  Dish.objects.all()
        serializer = DishesSerializer(dishes, many=True)

        if format is None :
            return render_to_response('ourapp/dishes.html', { 'dish_list' : dishes })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Dishes' : serializer.data})

@csrf_exempt
def dish_detail(request, pk, format=None):
    """
    Retrieve a dish's details.
    """
    try:
        dish = Dish.objects.get(pk = pk)
        customer_reviews = DishReview.objects.all().filter(dish = pk)
        similar_dishes = Dish.objects.all().filter(generic_dish = dish.generic_dish)
    except Dish.DoesNotExist:
        return HttpResponse(content='Dish not found', status=404)

    if request.method == 'GET':
        serializer = DishesSerializer(dish)

        if format is None :
            return render_to_response('ourapp/dish_attribute.html', { 'dish' : dish, 'customer_reviews':customer_reviews,'similar_dishes':similar_dishes})
        elif format.lower() == 'json' :
            return JSONResponse(serializer.data)

@csrf_exempt
def dish_reviews(request, pk, format=None):
    """
    Retrieve a Dish's reviews.
    """
    try:
        dish_reviews = DishReview.objects.all().filter(dish_id = pk)
    except DishReview.DoesNotExist:
        return HttpResponse(content='Dish not found', status=404)

    if request.method == 'GET':
        serializer = DishReviewsSerializer(dish_reviews, many=True)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse({'Dish Reviews' : serializer.data})

@csrf_exempt
def generic_dish_list(request, format=None):
    """
    List all Generic Dishes.
    """
    if request.method == 'GET':
        generic_dishes =  GenericDish.objects.all()
        serializer = GenericDishSerializer(generic_dishes, many=True)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Generic Dishes' : serializer.data})

@csrf_exempt
def generic_dish_detail(request, pk, format=None):
    """
    Retrieve a Generic Dish's details.
    """
    try:
        generic_dish = GenericDish.objects.get(pk = pk)
    except GenericDish.DoesNotExist:
        return HttpResponse(content='Generic Dish not found', status=404)

    if request.method == 'GET':
        serializer = GenericDishSerializer(generic_dish)

        if format is None:
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse(serializer.data)

@csrf_exempt
def generic_dish_dishes(request, pk, format=None):
    """
    Retrieve a Generic Dish's dishes.
    """
    try:
        generic_dish_dishes = Dish.objects.get(generic_dish_id = pk)
    except Dish.DoesNotExist:
        return HttpResponse(content='Dish not found', status=404)

    if request.method == 'GET':
        serializer = DishesSerializer(generic_dish_dishes)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Dishes' : serializer.data })

@csrf_exempt
def cuisine_list(request, format=None):
    """
    List all Cuisines.
    """
    if request.method == 'GET':
        cuisines =  Cuisine.objects.all()
        serializer = CuisineSerializer(cuisines, many=True)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Cuisines' : serializer.data })

@csrf_exempt
def cuisine_detail(request, pk, format=None):
    """
    Retrieve a cuisine's details.
    """
    try:
        cuisine = Cuisine.objects.get(pk = pk)
    except Cuisine.DoesNotExist:
        return HttpResponse(content='Dish not found', status=404)

    if request.method == 'GET':
        serializer = CuisineSerializer(cuisine)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse(serializer.data)

@csrf_exempt
def cuisine_restaurants(request, pk, format=None):
    """
    List all Cuisine's restaurants.
    """
    if request.method == 'GET':
        restaurants =  Restaurant.objects.all().filter(cuisine_id = pk)
        serializer = RestaurantSerializer(restaurants, many=True)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        if format.lower() == 'json' :
            return JSONResponse({ 'Cuisine Restuarants' : serializer.data })

@csrf_exempt
def cuisine_dishes(request, pk, format=None):
    """
    List all Cuisine's dishes.
    """
    if request.method == 'GET':
        dishes =  Dish.objects.all().filter(cuisine_id = pk)
        serializer = DishesSerializer(dishes, many=True)

        if format is None :
            return render_to_response('#.html', { 'result' : serializer.data })
        elif format.lower() == 'json' :
            return JSONResponse({ 'Cuisine Dishes' : serializer.data })