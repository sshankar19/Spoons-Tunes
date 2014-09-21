import facebook
import requests
from facebook import FacebookAPI, GraphAPI
from django.http import request

f = FacebookAPI(client_id='327860917388003', client_secret='2cfddeec2f1ad7abd1e4c5d103e29451',
                redirect_uri='http://darthbane.org')

auth_url = f.get_auth_url(scope=['publish_stream', 'user_photos', 'user_status'])
code = request
access_token = f.get_access_token(code)
print 'Connect with Facebook via: %s' % auth_url

#graph = facebook.GraphAPI("327860917388003|RbeGPTESdoXRubc0SFINQivA5Zo")
#profile = graph.get_object("me")
##friends = graph.get_connections("me", "friends")
#graph.put_object("me", "feed", message="I am writing on my wall!")


def getGenre(): 
    return

def getLocation():
    return