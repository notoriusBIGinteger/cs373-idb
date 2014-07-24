from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from ourapp.models import Dish, Restaurant

def home(request):
  dish_results = Dish.objects.order_by('name')[:5]
  restaurant_results =  Restaurant.objects.order_by('name')[:5]
  return render(request, 'ourapp/splash.html', {'dish_results':dish_results,'restaurant_results':restaurant_results})