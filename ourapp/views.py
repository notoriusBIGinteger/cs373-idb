from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from ourapp.models import Restaurant
from ourapp.serializers import *


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
def restaurant_list(request):
    """
    List all Restaurants.
    """
    if request.method == 'GET':
        restaurants =  Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)

        d = {"Restaurants" : serializer.data}

        return JSONResponse(d)

@csrf_exempt
def restaurant_detail(request, pk):
    """
    Retrieve a Restaurant.
    """
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Restaurant not found', status=404)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return JSONResponse(serializer.data)

@csrf_exempt
def restaurant_dishes(request, pk):
    """
    Retrieve a Restaurant's dishes.
    """
    try:
        restaurant_dishes = Dish.objects.all().filter(restaurant_id = pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Restaurant not found', status=404)

    if request.method == 'GET':
        serializer = DishesSerializer(restaurant_dishes, many=True)

        res = { 'restaurant_dishes' : serializer.data }

        return JSONResponse(res)

@csrf_exempt
def restaurant_reviews(request, pk):
    """
    Retrieve a Restaurant's dishes.
    """
    try:
        restaurant_reviews = RestaurantReview.objects.all().filter(restaurant_id = pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Restaurant not found', status=404)

    if request.method == 'GET':
        serializer = RestaurantReviewsSerializer(restaurant_reviews, many=True)

        d = {"restaurant_reviews" : serializer.data}

        return JSONResponse(d)

@csrf_exempt
def customer_list(request):
    """
    List all Customers.
    """
    if request.method == 'GET':
        customers =  Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        d = {"Customers" : serializer.data}

        return JSONResponse(d)

@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve a Customer.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Customer not found', status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JSONResponse(serializer.data)

@csrf_exempt
def customer_restaurant_reviews(request, pk):
    """
    Retrieve a Customer's reviews.
    """
    try:
        customer_r_reviews = RestaurantReview.objects.get(customer_id = pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Customer not found', status=404)

    if request.method == 'GET':
        serializer = RestaurantReviewsSerializer(customer_r_reviews)

        d = {'customer_restaurant_reviews' : serializer.data}

        return JSONResponse(d)

@csrf_exempt
def customer_dish_reviews(request, pk):
    """
    Retrieve a Customer's reviews.
    """
    try:
        customer_d_reviews = DishReview.objects.get(customer_id = pk)
    except Restaurant.DoesNotExist:
        return HttpResponse(content='Customer not found', status=404)

    if request.method == 'GET':
        serializer = DishReviewsSerializer(customer_d_reviews)

        d = {'customer_dish_reviews' : serializer.data}

        return JSONResponse(d)
