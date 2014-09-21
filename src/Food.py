import json
import ordrin
from pprint import pprint
from Queue import PriorityQueue, Queue

class Eatery:
    i = 0;
    def __init__(self):
        i = 0;

class Food:
    i = 0;
    def __init__(self):
        i = 0;

json_data=open('genres2.json')

data = json.load(json_data)
#pprint(data)
genre_data = data['genres']
list = []
value = []
i = 0
for d in genre_data: 
    list.append(d["name"])
    value.append(i)
    i+=1
    if(i == 10):
        i = 0
    
    #print '\n'
json_data.close()
 

#for e in list:
#   print e + "\n"    

def order(food, location,city,zipcode, price):
    ordrin_api = ordrin.APIs('VP0cjZmpyVPNAFJUJkBWDIETChyTTwp7mX3jlPzfn4Q', ordrin.TEST)
    restaurants =  ordrin_api.delivery_list("ASAP", location, city, zipcode)
    
    priority = PriorityQueue()
    
    for r in restaurants:
#pprint(r)
#print r['id']
        temp = ordrin_api.restaurant_details(str(r['id']))
#pprint(temp)
        cuisines = temp['cuisine']
        highpriority = False
        j = 0
        for j in range(len(cuisines)):
#print cuisines[j]
            if cuisines[j] is food:
                highpriority = True;
         
        restauPair = {}       
        pprint(temp)
        menu = temp['menu']
        menuItems = menu[0]
       #pprint(menuItems)
        additionalfee = menuItems['additional_fee']
        children = menuItems['children'] 
        #print(additionalfee)
        #pprint(menu)
        for child in children: #each individual plate of food
            addFeePerItem = child['additional_fee']
            descrip = child['descrip']
            ID = child['id']
            name = child['name']
            price = child['price']
            #pprint (child)
                
        if highpriority:
            priority.put(1, temp)
        else:
            priority.put(2, temp)
            

    top = priority.get_nowait()
    
    
    #IDENTIFY THE TOP RESTAURANT. NOW WE HAVE TO ASK THE USER WHAT THEY WANT.
    
    
    #get all of the stuff in priority of the food.
    
    

def getFood(genre, location,city, zipcode, price):
    b = list.index("rap")
    print b
    k = value[b];
    
    print k
    k = 0
    food = None;
    if k == 0:
        food = "pizza"
    elif k == 1:
        food = "pasta"
    elif k == 2:
        food = "steak"
    elif k == 3:
        food = "Chinese"
    elif k == 4:
        food = "salad"
    elif k== 5:
        food = "shepherd's pie"
    elif k== 6:
        food = "Banh Mi"
    elif k ==7:
        food = "Japanese"
    elif k==8:
        food = "sandwiches"
    elif k==9:
        food = "bratwurst"
        
    """" yelp_api = YelpAPI("f17enpkvjgN00WkXxWj_Lg", "_4C-O6y3XpCxsJ_QedKYP0rpW_c", "cXAjo9c62IM6po_TL3vAvaJ73gZH00qb", "Ro3VGHHrr1rPFagUDCnJBtOmHiw" )
    response = yelp_api.search_query(term='food', location=location, sort=1, limit=20, radius_filter="20000")
    
    print('region center (lat,long): %f,%f\n' % (response['region']['center']['latitude'], response['region']['center']['longitude']))
    for business in response['businesses']:
        print('%s\n\tYelp ID: %s\n\trating: %g (%d reviews)\n\taddress: %s' % (business['name'], business['id'], business['rating'],
                                                                    business['review_count'], ', '.join(business['location']['display_address'])))
   """
    order(food, location, city, zipcode, price)
    
print "here"    
getFood("rap", "10 7th Avenue", "New York City", "10001", "3.28")

    #set food according to genre
    #use yelp to find 
        #use location to 