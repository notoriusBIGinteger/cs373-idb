from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dish(request, dishID):
  responseString = "hi you are viewing dishID: " + str(dishID)
  return HttpResponse(responseString)

def restaurant(request, restaurantID):
  responseString = "hi you are viewing restaurantID: " + str(restaurantID)
  return HttpResponse(responseString)

def customer(request, customerID):
  responseString = "hi you are viewing customerID: " + str(customerID)
  return HttpResponse(responseString)
