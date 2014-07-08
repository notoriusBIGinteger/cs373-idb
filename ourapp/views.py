from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer(request, customerID):
  context = {}
  return render(request, 'ourapp/customer.html', context)

def dish(request, dishID):
  context = {}
  return render(request, 'ourapp/dish.html', context)

def restaurant(request, restaurantID):
  context = {}
  return render(request, 'ourapp/restaurant.html', context)
