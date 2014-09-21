import json
import ordrin
from pprint import pprint
from yelpapi import YelpAPI
from Queue import PriorityQueue, Queue


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
 

for e in list:
    print e + "\n"    

def order(food, location,city,zipcode, price):
    ordrin_api = ordrin.APIs('VP0cjZmpyVPNAFJUJkBWDIETChyTTwp7mX3jlPzfn4Q', ordrin.TEST)
    restaurants =  ordrin_api.delivery_list("ASAP", location, city, zipcode)
    
    priority = PriorityQueue()
    
    for r in restaurants:
        temp = ordrin_api.restaurant_details(r[id])
        cuisines = json.loads(temp)['cuisine']
        if cuisines is food:
            priority.put(1, temp)
        elif cuisines:    
            priority.put(2, temp)
           
    menu = []
    restauPair = {}       
            
    for t in priority:
        for item in (t['menu'])['children']:
            for children in item:
                for food in children:
                    print food['price']
                    restauPair.update({t:food})

    top = priority.get_nowait()
    
    
    #IDENTIFY THE TOP RESTAURANT. NOW WE HAVE TO ASK THE USER WHAT THEY WANT.
    
    
    #get all of the stuff in priority of the food.
    
    

def getFood(genre, location,city, zipcode, price):
    i = list.index(genre )
    k = value[i]
    food = None;
    if k == 0:
        food = "pizza"
    elif k == 1:
        food = "pasta"
    elif k == 2:
        food = "steak"
    elif k == 3:
        food = "sushi"
    elif k == 4:
        food = "salad"
    elif k== 5:
        food = "shepherd's pie"
    elif k== 6:
        food = "Banh Mi"
    elif k ==7:
        food = "asian"
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