from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

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
