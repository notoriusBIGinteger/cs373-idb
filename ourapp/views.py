from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from ourapp.models import *
from ourapp.serializers import *
from twitter import *
import json
import requests
from django.core.urlresolvers import reverse

def splash(request):
    context = {}
    return render(request, 'ourapp/splash.html', context)

def rest(request):
  context = {}
  return render(request, 'ourapp/rest.html', context)

def index(request):
  context = {}
  return render(request, 'ourapp/index.html', context)

class JSONResponse(HttpResponse) :
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        #content = JSONRenderer().render(data, , renderer_context = {'indent' : 4})
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def restaurant_list(request, format=None):
    """
    Get all a list of Restaurants.
    """
    try :
        restaurants = Restaurant.objects.all()

        if len(restaurants) == 0 :
            raise Restaurant.DoesNotExist

    except Restaurant.DoesNotExist :
        if format is None :
            return HttpResponse(content='No restaurants found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No restaurants found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/restaurant.html', { 'restaurants_result' : restaurants })
        elif format.lower() == 'json' :
            serializer = RestaurantSerializer(restaurants, many=True)
            return JSONResponse(serializer.data)

@csrf_exempt
def restaurant_detail(request, pk, format=None):
    """
    Retrieve a Restaurant's details.
    """
    rest = {"1":"#hydeparkbarandgrill","2":"#magnoliacafe","3":"#changthai"}
    try:
        restaurant = Restaurant.objects.get(id = pk)
        dish_results = Dish.objects.all().filter(restaurant = pk)
        customer_reviews = RestaurantReview.objects.all().filter(restaurant = pk)
        t = Twitter(
            auth=OAuth('2678149836-qlByM0SSADzChlFzrcZsmvQagsjhOqCm1lgON87', 'QuqqOy5N9xlHRnmQk7W88nA9yLtG3CgnNXfV0avcsXwwg',
                       'BqmrjxAmBB6YzG5qsoWEcpMvg', 'ZosP5zX4h3AD9zBc6YFaHoLZw9WSognRqGeF6uz7PYGmGyDaeJ')
           )
        name_lower = restaurant.name.replace(" ", "")
        name = "#" + name_lower
        d = json.loads(json.dumps(t.search.tweets(q="#hello", count=5)))
        twitter_response = []
        for line in d["statuses"]:
            twitter_response.append((line["user"]["name"],line["text"]))


    except Restaurant.DoesNotExist:
        if format is None :
            return HttpResponse(content='No restaurant found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No restaurant found.'})

    if request.method == 'GET':
        if format is None :
            #return StreamingHttpResponse(twitter_response)
            return render_to_response('ourapp/restaurant_attributes.html', { 'restaurant' : restaurant , 'dish_results' : dish_results,
            'customer_reviews' : customer_reviews, 'twitter_response': twitter_response,})
        elif format.lower() == 'json' :
            serializer = RestaurantSerializer(restaurant)
            return JSONResponse(serializer.data)

@csrf_exempt
def restaurant_dishes(request, pk, format=None):
    """
    Retrieve a Restaurant's dishes.
    """
    try:
        restaurant_dishes = Dish.objects.all().filter(restaurant_id = pk)

        if len(restaurant_dishes) == 0 :
            raise Dish.DoesNotExist

        restaurant = Restaurant.objects.get(id = pk)
    except (Dish.DoesNotExist, Restaurant.DoesNotExist):
        if format is None :
            return HttpResponse(content='No restaurant dishes found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No restaurant dishes found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/restaurant_dishes.html', { 'restaurant_dishes' : restaurant_dishes, 'restaurant' : restaurant })
        elif format.lower() == 'json' :
            serializer = DishesSerializer(restaurant_dishes, many=True)
            return JSONResponse( { 'Restaurant Dishes' : serializer.data} )

@csrf_exempt
def restaurant_reviews(request, pk, format=None):
    """
    Retrieve a Restaurant's reviews.
    """
    try:
        customer_reviews = RestaurantReview.objects.all().filter(restaurant = pk)

        if len(customer_reviews) == 0 :
            raise RestaurantReview.DoesNotExist

        restaurant = Restaurant.objects.get(pk = pk)
    except (RestaurantReview.DoesNotExist, Restaurant.DoesNotExist):
        if format is None :
            return HttpResponse(content='No restaurant reviews found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No restaurant reviews found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/restaurant_reviews.html', { 'customer_reviews' : customer_reviews, 'restaurant' : restaurant })
        elif format.lower() == 'json' :
            serializer = RestaurantReviewsSerializer(customer_reviews, many=True)
            return JSONResponse({ 'Restaurant Reviews' : serializer.data })

@csrf_exempt
def customer_list(request, format=None):
    """
    List all Customers.
    """
    try :
        customers = Customer.objects.all()

        if len(customers) == 0 :
            raise Customer.DoesNotExist

    except Customer.DoesNotExist :
        if format is None :
            return HttpResponse(content='No customers found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No customers found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/customer.html', { 'customers_result' : customers })
        elif format.lower() == 'json' :
            serializer = CustomerSerializer(customers, many=True)
            return JSONResponse({ 'Customers' : serializer.data })

@csrf_exempt
def customer_detail(request, pk, format=None):
    """
    Retrieve a Customer.
    """
    try:
        customer = Customer.objects.get(id = pk)
        dish_reviews = DishReview.objects.all().filter(customer = pk)[:5]
        restaurant_reviews = RestaurantReview.objects.all().filter(customer = pk)[:5]
    except Customer.DoesNotExist:
        if format is None :
            return HttpResponse(content='No customer found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No customer found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/customer_attributes.html', {'customer' : customer , 'dish_reviews' : dish_reviews,
            'restaurant_reviews' : restaurant_reviews})
        elif format.lower() == 'json' :
            serializer = CustomerSerializer(customer)
            return JSONResponse(serializer.data)

@csrf_exempt
def customer_restaurant_reviews(request, pk, format=None):
    """
    Retrieve a Customer's reviews.
    """
    try:
        customer_r_reviews = RestaurantReview.objects.all().filter(customer_id = pk)

        if len(customer_r_reviews) == 0 :
            raise RestaurantReview.DoesNotExist

        customer = Customer.objects.get(id = pk)
    except (RestaurantReview.DoesNotExist, Customer.DoesNotExist):
        if format is None :
            return HttpResponse(content='No customer restaurant reviews found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No customer restaurant reviews found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/customer_restaurant_reviews.html', { 'customer_r_reviews' : customer_r_reviews,
            'customer':customer})
        elif format.lower() == 'json' :
            serializer = RestaurantReviewsSerializer(customer_r_reviews, many=True)
            return JSONResponse({ 'Customer Restaurant Reviews' : serializer.data })

@csrf_exempt
def customer_dish_reviews(request, pk, format=None):
    """
    Retrieve a Customer's reviews.
    """
    try :
        customer_d_reviews = DishReview.objects.all().filter(customer_id = pk)
        customer = Customer.objects.get(id = pk)

        if (customer_d_reviews ==0) :
            raise DishReview.DoesNotExist

    except (Customer.DoesNotExist, DishReview.DoesNotExist) :
        if format is None :
            return HttpResponse(content='No customer dish reviews found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No customer dish reviews found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/customer_dish_reviews.html', { 'customer_d_reviews' : customer_d_reviews, 'customer':customer })
        elif format.lower() == 'json' :
            serializer = DishReviewsSerializer(customer_d_reviews, many=True)
            return JSONResponse({ 'Customer Dish Reviews' : serializer.data })

@csrf_exempt
def dish_list(request, format=None):
    """
    List all Dishes.
    """
    try :
        dishes = Dish.objects.all()

        if len(dishes) == 0 :
            raise Dish.DoesNotExist

    except Dish.DoesNotExist :
        if format is None :
            return HttpResponse(content='No dishes found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No dishes found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/dishes.html', { 'dish_list' : dishes })
        elif format.lower() == 'json' :
            serializer = DishesSerializer(dishes, many=True)
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
    except Dish.DoesNotExist :
        if format is None :
            return HttpResponse(content='No dish found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No dish found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/dish_attribute.html', { 'dish' : dish, 'customer_reviews' : customer_reviews,
            'similar_dishes' : similar_dishes})
        elif format.lower() == 'json' :
            serializer = DishesSerializer(dish)
            return JSONResponse(serializer.data)

@csrf_exempt
def dish_reviews(request, pk, format=None):
    """
    Retrieve a Dish's reviews.
    """
    try:
        dish_reviews = DishReview.objects.all().filter(dish_id = pk)
        dish = Dish.objects.get(id = pk)

        if len(dish_reviews) == 0 :
            raise Dish.DoesNotExist

    except Dish.DoesNotExist:
        if format is None :
            return HttpResponse(content='No dish reviews found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No dish reviews found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/dish_reviews.html', { 'dish_reviews' : dish_reviews, 'dish':dish })
        elif format.lower() == 'json' :
            serializer = DishReviewsSerializer(dish_reviews, many=True)
            return JSONResponse({'Dish Reviews' : serializer.data})

@csrf_exempt
def generic_dish_list(request, format=None):
    """
    List all Generic Dishes.
    """
    try :
        generic_dishes = GenericDish.objects.all()

        if len(generic_dishes) == 0 :
            raise GenericDish.DoesNotExist

    except GenericDish.DoesNotExist :
        if format is None :
            return HttpResponse(content='No generic dishes found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No generic dishes found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/generic_dish_list.html', { 'generic_dishes_result' : generic_dishes })
        elif format.lower() == 'json' :
            serializer = GenericDishSerializer(generic_dishes, many=True)
            return JSONResponse({ 'Generic Dishes' : serializer.data})

@csrf_exempt
def generic_dish_detail(request, pk, format=None):
    """
    Retrieve a Generic Dish's details.
    """
    try :
        generic_dish = GenericDish.objects.get(id = pk)
        generic_dish_dishes = Dish.objects.all().filter(generic_dish = generic_dish)
        restaurant_results = []
        for dish in generic_dish_dishes:
            rest = Restaurant.objects.get(pk = dish.restaurant.id)
            if not rest in restaurant_results:
                restaurant_results.append(rest)
    except GenericDish.DoesNotExist :
        if format is None :
            return HttpResponse(content='No generic dish found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No generic dish found.'})

    if request.method == 'GET':
        if format is None:
            return render_to_response('ourapp/generic_dish_detail.html',{ 'generic_dish_name' : generic_dish.name ,
            'dish_results' : generic_dish_dishes, 'restaurant_results' :  restaurant_results })
        elif format.lower() == 'json' :
            serializer = GenericDishSerializer(generic_dish)
            return JSONResponse(serializer.data)

@csrf_exempt
def generic_dish_dishes(request, pk, format=None):
    """
    Retrieve a Generic Dish's dishes.
    """
    try:
        generic_dish_dishes = Dish.objects.all().filter(generic_dish_id = pk)

        if len(generic_dish_dishes) == 0 :
            raise GenericDish.DoesNotExist

        g_name = GenericDish.objects.get(id = pk).name
    except GenericDish.DoesNotExist :
        if format is None :
            return HttpResponse(content='No generic dish dishes found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No generic dish dishes found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/generic_dish_dishes.html', { 'generic_dish_name' : g_name,
            'generic_dish_dishes_result' : generic_dish_dishes })
        elif format.lower() == 'json' :
            serializer = DishesSerializer(generic_dish_dishes, many=True)
            return JSONResponse({ 'Dishes' : serializer.data })

@csrf_exempt
def cuisine_list(request, format=None):
    """
    List all Cuisines.
    """
    try :
        cuisines = Cuisine.objects.all()

        if len(cuisines) == 0 :
            raise Cuisine.DoesNotExist

    except Cuisine.DoesNotExist :
        if format is None :
            return HttpResponse(content='No cuisines found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No cuisines found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/cuisines.html', { 'cuisine_result' : cuisines })
        elif format.lower() == 'json' :
            serializer = CuisineSerializer(cuisines, many=True)
            return JSONResponse({ 'Cuisines' : serializer.data })

@csrf_exempt
def cuisine_detail(request, pk, format=None):
    """
    Retrieve a cuisine's details.
    """
    try:
        cuisine = Cuisine.objects.get(id = pk)
        dish_results = Dish.objects.all().filter(cuisine = cuisine)[:5]
        restaurant_results = []#Restaurant.objects.all().filter(cuisine = cuisine)[:5]
        for d in dish_results:
            r = Restaurant.objects.get(pk = d.restaurant.id)
            if not r in restaurant_results:
                restaurant_results.append(r)
        rest = Restaurant.objects.all().filter(cuisine = cuisine)
        for r in rest:
            if not r in restaurant_results:
                restaurant_results.append(r)
        generic_results = GenericDish.objects.all().filter(cuisine = cuisine)[:5]
    except Cuisine.DoesNotExist :
        if format is None :
            return HttpResponse(content='No cuisine found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No cuisine found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/cuisine_detail.html', { 'cuisine' : cuisine, 'dish_results' : dish_results,
            'restaurant_results' : restaurant_results, 'generic_results' : generic_results })
        elif format.lower() == 'json' :
            serializer = CuisineSerializer(cuisine)
            return JSONResponse(serializer.data)

@csrf_exempt
def cuisine_restaurants(request, pk, format=None):
    """
    List all Cuisine's restaurants.
    """
    try :
        restaurants = Restaurant.objects.all().filter(cuisine_id = pk)

        if len(restaurants) == 0 :
            raise Restaurant.DoesNotExist

    except Restaurant.DoesNotExist :
        if format is None :
            return HttpResponse(content='No cuisine restaurants found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No cuisine restaurants found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/cuisine_restaurants.html', { 'dish_restaurant' : restaurants })
        if format.lower() == 'json' :
            serializer = RestaurantSerializer(restaurants, many=True)
            return JSONResponse({ 'Cuisine Restaurants' : serializer.data })

@csrf_exempt
def cuisine_dishes(request, pk, format=None):
    """
    List a Cuisine's dishes.
    """
    try :
        dishes = Dish.objects.all().filter(cuisine_id = pk)

        if len(dishes) == 0 :
            raise Dish.DoesNotExist

    except Dish.DoesNotExist :
        if format is None :
            return HttpResponse(content='No cuisine dishes found.', status=404)
        elif format.lower() == 'json' :
            return JSONResponse({'Error' : 'No cuisine dishes found.'})

    if request.method == 'GET':
        if format is None :
            return render_to_response('ourapp/cuisine_dishes.html', { 'dish_result' : dishes })
        elif format.lower() == 'json' :
            serializer = DishesSerializer(dishes, many=True)
            return JSONResponse({ 'Cuisine Dishes' : serializer.data })

@csrf_exempt
def about(request):
    """
    Render the "about us" page.
    """
    return render(request, 'ourapp/about_us.html')

@csrf_exempt
def the_austinites(request) :
    """
    Request all data from the Austinites API and store in dictionary, then
    render HTML response.
    """
    api_data = {}
    api_data['all'] = {'stages' : None, 'sponsors' : None, 'artists' : None}

    for k in api_data['all'] :
	    x = requests.get("http://theaustinites.pythonanywhere.com/api/" + k + "/")
	    api_data['all'][k] = x.json()
	    x.close()

    for k in api_data['all'] :
	    for d in api_data['all'][k] :
		    x = requests.get("http://theaustinites.pythonanywhere.com/api/" + k + "/"
			    + str(d['id']) + "/media/")
		    d['media'] = x.json()
		    x.close()

    return render_to_response('ourapp/nathan_test.html', { 'austinitesAPI' : api_data['all'] } )

@csrf_exempt
def search_results(request) :
    """
    Render the "about us" page.
    """
    return render(request, 'ourapp/results.html')


def normalize_query(query_string):
    return query_string.lower().split()


#def get_and_query(terms, search_fields): # changed to take terms directly instead of string.
#    ''' Returns a query, that is a combination of Q objects. That combination
#    aims to search keywords within a model by testing the given search fields.
#
#    '''
#    query = None # Query to search for every search term
#    for term in terms:
#        or_query = None # Query to search for a given term in each field
#        for field_name in search_fields: # if any of the fields contain it.
#            q = Q(**{"%s__icontains" % field_name: term})
#            if or_query is None:
#                or_query = q
#            else:
#                or_query = or_query | q
#        if query is None:
#            query = or_query
#        else:
#            query = query & or_query
#    return query
#
#def get_or_query(terms, search_fields): # changed to take terms directly instead of string.
#    ''' Returns a query, that is a combination of Q objects. That combination
#    aims to search keywords within a model by testing the given search fields.
#
#    '''
#    query = None # Query to search for every search term
#    for term in terms:
#        or_query = None # Query to search for a given term in each field
#        for field_name in search_fields: # if any of the fields contain it.
#            q = Q(**{"%s__icontains" % field_name: term})
#            if or_query is None:
#                or_query = q
#            else:
#                or_query = or_query | q
#        if query is None:
#            query = or_query
#        else:
#            query = query & or_query
#    return query
#
#def getDishAndInstances(terms):
#    andQObject = get_and_query(terms, ['name', 'description'])
#    return Dish.objects.filter(andQObject)
#
#def getRestAndInstances(terms):
#    andQObject = get_and_query(terms, ['name', 'description'])
#    return Restaurant.objects.filter(andQObject)
#
#def getDishOrInstances(terms):
#    andQObject = get_or_query(terms, ['name', 'description'])
#    return Dish.objects.filter(andQObject)
#
#def getRestOrInstances(terms):
#    andQObject = get_or_query(terms, ['name', 'description'])
#    return Restaurant.objects.filter(andQObject)
#
#def getDishResults(inst, terms, resultDict):
#    """given a dish instance, a list of search terms, and a dictionary
#    where the keys are url strings, and the values are search result text
#    strings for the corresponding url, update the dictionary TODO.'
#    inst = Dish objects
#    terms = ['name','description']
#    {'url':'text...'}
#    """
#    # first see if this object is already in the result
#    # if it is, append to the text, if not create it.
#    url = reverse('adishjson',args=[inst.id])
#    text = inst.name + "..." + inst.description + "..."
#    if url in resultDict:
#        resultDict[url] = text + resultDict[url]
#    else:
#        resultDict[url] = text
#
#    #Now handle all the dishes similar to the inst object
#    similar_dishes = Dish.objects.all().filter(generic_dish = inst.generic_dish)
#    for dish in similar_dishes:
#        if dish.name != inst.name:
#            url = reverse('adishjson',args=[dish.id])
#            text = "Similar Dishes..." + inst.name + "..."
#
#            if url in resultDict:
#                resultDict[url] += text
#            else:
#                resultDict[url] = text
#
#    return resultDict
#
#def getRestResults(inst, terms, resultDict):
#    """given a dish instance, a list of search terms, and a dictionary
#    where the keys are url strings, and the values are search result text
#    strings for the corresponding url, update the dictionary TODO.
#    """
#    url = reverse('arestjson', args=[inst.id])
#    resultDict[url] = {'stub. rest name = ' + inst.name}
#
#def getAndInstances(terms):
#    retList = []
#    retList += list(getDishAndInstances(terms))
#    retList += list(getRestAndInstances(terms))
#    return retList
#
#def getOrInstances(terms):
#    retList = []
#    retList += list(getDishOrInstances(terms))
#    retList += list(getRestOrInstances(terms))
#    return retList
#
#def getAndResults(andInstanceList, terms):
#    result = {}
#    for inst in andInstanceList:
#        if type(inst) == Dish:
#            getDishResults(inst, terms, result)
#        if type(inst) == Restaurant:
#            getRestResults(inst, terms, result)
#    return result
#
#def getOrResults(orInstanceList, terms):
#    result = {}
#    for inst in orInstanceList:
#        if type(inst) == Dish:
#            getDishResults(inst, terms, result)
#        if type(inst) == Restaurant:
#            getRestResults(inst, terms, result)
#    return result

def urlContentPairs(request):
    """
    Input a HttpRequest just so we have something to call our views with.
    Returns a generator that yields length two tuples. The first element of
    the tuple will be a url and the second element will be a string with
    the contents the html document associated with that url (with all html
    tags, css, javascript still included).
    """
    for rest in Restaurant.objects.all():
        restUrl = reverse('arestjson', args=[rest.id])
        html = restaurant_detail(request, rest.id).content
        yield (restUrl, html)

    for dish in Dish.objects.all():
        dishUrl = reverse('adishjson', args=[dish.id])
        html = dish_detail(request, dish.id).content
        yield (dishUrl, html)

    indexUrl = reverse('index')
    html = index(request).content
    yield (indexUrl, html)

    aboutUrl = reverse('about')
    html = about(request).content
    yield (aboutUrl, html)


def urlStrippedContentPairs(request, terms):
    """
    Input: a generator that yields length two tuples, the first element will be
    a URL and the second element will be the html/css/javascript content of that
    URL.

    Also input a request just so urlContentPairs() has something to call 
    views with.

    Output: a generator that yields length two tuples, the first element will
    be a URL, and the second element will be the a list of paragraphs from that URL
    without any html/css/javascript.
    """
    urlContentGen = urlContentPairs(request)
    for url, content in urlContentGen:
        yield (url, list(myStrip(content, terms)))

def getPattern(terms):
    """ Given a list of terms, constructs a pattern that matches any of the terms """
    patternStr = "("
    for term in terms:
        patternStr += term + "|"
    patternStr = patternStr[:-1] #chop of extra "|" character
    patternStr += ")"
    pat = re.compile(patternStr)
    return pat

def myStrip(string, terms):
    """ Given an html document sent as a string, strips out all of the
    html/css/javscript and return a generator that yields paragraphs
    without html/css/javascript. Only returns paragraphs that contain a match.
    """
    soup = BeautifulSoup(string)
    pat = getPattern(terms)
    for p_tag in soup.find_all('p'):
        yield str(p_tag.text)

def andResultsBlah(pList, terms):
    """
       Takes in a list of paragraph strings and an iterable of terms to search for. If the string
       contains all of the terms then it will return the string with tags
       around the matched terms. Else returns None.
    """
    string = ''.join(pList)
    lowerString = string.lower()
    for term in terms:
        if not term in lowerString:
            return None
    return string

def orResultsBlah(pList, terms):
    """
       Takes in a list of paragraph strings and a list of terms to search for. If the string
       contains any of the terms then it will return the string with tags
       around the matched terms. Else returns None.
    """
    string = ''.join(pList)
    lowerString = string.lower()
    foundSomething = False
    for term in terms:
        if term in lowerString:
            foundSomething = True
            break

    if not foundSomething:
        return None

    return string

def addTags(string, terms):
    """
       Given a string and an iterable of terms (each term is a string), returns the string except with 
       tags around any instances of any of the terms.
    """
    if not terms: #TODO think this through?
        return string

    def tag(match):
        return "<strong>" + match.group() + "</strong>"

    pat = getPattern(terms)
    retString = pat.sub(tag, string)
    return retString

def search(request, string):
   # address="http://notoriousbiginteger.pythonanywhere.com/restaurants/1/"
   # html = urlopen(address).read()
#    try:
        terms = normalize_query(string)
        urlsAndStrippedConts = urlStrippedContentPairs(request, terms)
        orResults = []
        andResults = []
        for url, textList in urlsAndStrippedConts:
            andResultStr = andResultsBlah(textList, terms)
            if andResultStr:
                andResultStr = addTags(andResultStr, terms)
                andResults.append((url, andResultStr)) 
                
            orResultStr = orResultsBlah(textList, terms)
            if orResultStr:
                orResultStr = addTags(orResultStr, terms)
                orResults.append((url, orResultStr)) 

        finalResults = [andResults, orResults]
        return HttpResponse(json.dumps(finalResults), content_type="application/json")
        
#    except Exception:
#        return HttpResponse(str([[],[]]))















