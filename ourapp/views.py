from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def customer(request, customerID):
  customerIDInt = int(customerID) #make int so 1, 01, or 001, all work.
  context = {}
  if customerIDInt == 1:
    return render(request, 'ourapp/customer1.html', context)
  elif customerIDInt == 2:
    return render(request, 'ourapp/customer2.html', context)
  else:
    raise Http404

def dish(request, dishID):
  dishIDInt = int(dishID) #make int so 1, 01, or 001, all work.
  context = {}
  if dishIDInt == 1:
    return render(request, 'ourapp/dish1.html', context)
  elif dishIDInt == 2:
    return render(request, 'ourapp/dish2.html', context)
  else:
    raise Http404

def restaurant(request, restaurantID):
  restaurantIDInt = int(restaurantID) #make int so 1, 01, or 001, all work.
  context = {}
  if restaurantIDInt == 1:
    return render(request, 'ourapp/restaurant1.html', context)
  elif restaurantIDInt == 2:
    return render(request, 'ourapp/restaurant2.html', context)
  else:
    raise Http404

def index(request):
  context = {}
  return render(request, 'ourapp/index.html', context)
