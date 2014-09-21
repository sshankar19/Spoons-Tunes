import json
import ordrin
from pprint import pprint
from Queue import PriorityQueue, Queue

class Eatery:
    def __init__(self, name, priority, ID):
        self.name = name;
        self.priority = priority;
        
class Food:
    def __init__(self, addFeePerItem, descrip, ID, name, price,rid):
        self.addFeePerItem = addFeePerItem;
        self.descrip = descrip;
        self.ID = ID;
        self.name = name;
        self.price = price
        self.rid = rid;

json_data=open('genres2.json')

data = json.load(json_data)
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

json_data.close()


def printFood(list):
    for item in list:
        print "\tName is: "+item.name
        print "\t\tDescription is: " + item.descrip;
        print "\t\tPrice is: "+item.price

def selectItem(list):
    item = raw_input("What would you like to order then?")
    for choice in list:
        if item == choice.name:
            return choice
        

def suggestionMenu(restDict, restaurant, ordrin):
    print "Your choices are the following: "
    print "\n"
    list = restDict[restaurant['name']]
    print "\n"
    
    printFood(list)
    choice = selectItem(list)
    totalFood = [];
    totalFood.append(choice)
    
    more = raw_input("Do you want to order another item? Enter yes or no.")
    while(more == "yes"):
        choice = selectItem(list)
        totalFood = [];
        totalFood.append(choice)
        more = raw_input("Do you want to order another item? Enter yes or no.")
    
    return totalFood

def selectRestaurant(priority):
    restaurant = priority.get_nowait();
    print restaurant
    print "The restaurant suggested is: "+ restaurant['name']
    return restaurant
    
def finalOrder(restDict, priority, ordrin):
    print("Here")
    restaurant = selectRestaurant(priority)
    confirmation = raw_input("Do you want to order from here? Enter yes or no.");
    print("there")
    if confirmation is "yes":
        totalFood = suggestionMenu(restDict, restaurant, ordrin)
    else:
        while(confirmation != "yes"):
            restaurant = selectRestaurant(priority)
            confirmation = raw_input("Do you want to order from here? Enter yes or no.");
        if confirmation != "yes":
            print "Sorry we couldn't find a restaurant to your liking. Please try again"
            return;
        else:
            totalFood = suggestionMenu(restDict, restaurant, ordrin)
    
    #make tray
    tray = ""
    for food in totalFood:
        tray = food.name+"/1+";
    tray = tray[:(len(tray)-1)]
    #pprint (restaurant)

    ordrin.order_guest(totalFood[0].rid, "em@em.com", tray, "5.05", "Example", "User", "2345678901", "77840", "1 Main Street", "College Station", "TX", "4111111111111111", "123", "02/2016", "1 Main Street", "College Station", "TX", "77840", "2345678901",  "", "", "", "ASAP", "ASAP")
    
    #time to order the food items
    
        


def order(food, location,city,zipcode):
    ordrin_api = ordrin.APIs('VP0cjZmpyVPNAFJUJkBWDIETChyTTwp7mX3jlPzfn4Q', ordrin.TEST)
    restaurants =  ordrin_api.delivery_list("ASAP", location, city, zipcode)
    
    priorityQ = PriorityQueue()
    restauPair = {}     
    for r in restaurants:
#pprint(r)
        rid = str(r['id'])
        temp = ordrin_api.restaurant_details(str(r['id']))
#pprint(temp)
        cuisines = temp['cuisine']
        highpriority = False
        j = 0
        for j in range(len(cuisines)):
#print cuisines[j]
            if cuisines[j] is food:
                highpriority = True;
        
         
        if highpriority:
            priority = 1
        else:
            priority = 2         
         
        #newRest = Eatery(temp['name'], priority)  
        foodList = [];
        #pprint(temp)
        menuItems = (temp['menu'])[0]#go through ALL menu Items
       #pprint(menuItems)
        additionalfee = menuItems['additional_fee']
        children = menuItems['children'] 
        #print(additionalfee)
        #pprint(menu)
        for child in children: #each individual plate of food #Go through ALL combinations of individual plate of food
            addFeePerItem = child['additional_fee']
            descrip = child['descrip']
            ID = child['id']
            name = child['name']
            price = child['price']
            newFood = Food(addFeePerItem, descrip, ID, name, price, rid)
            foodList.append(newFood)
            #print newFood.ID
            #pprint (child)
        
        restauPair[temp['name']] = foodList
        priorityQ.put(temp, priority)
        #restauPair[newRest] = foodList        
    finalOrder(restauPair, priorityQ, ordrin_api)   
    #IDENTIFY THE TOP RESTAURANT. NOW WE HAVE TO ASK THE USER WHAT THEY WANT.
       #get all of the stuff in priority of the food.
    
    

def getFood(genre, location,city, zipcode):
    b = list.index(genre)
    #print b
    k = value[b];
    
    #print k
    #k = 0
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
    order(food, location, city, zipcode)
    
getFood("rap", "10 7th Avenue", "New York City", "10001")

    #set food according to genre
    #use yelp to find 
        #use location to 