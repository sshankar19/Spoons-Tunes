#ask the user the event (location, city, zipcode)
import Music
import Spotify
import pyechonest
import spotipy

print "Welcome to Spoons&Tunes"
print "Spoons&Tunes helps to organize your event, by:"
print "    1) Making a Spotify playlist custom for your hangout based on your personal taste and bands in your area."
print "    2) Finding the perfect food choice for you to order (cater) Food from by using the ordr.in API"
#print "    3) Tweeting to your friends on twitter and letting them know about your hangout!

location = raw_input("Please enter the address of your event:")
#print location
city = raw_input("Now the city please:")
#print city
state = raw_input("State of residence please!")
#print state
zipcode = raw_input("Please enter the zipcode of your event:")
#print zipcode
username = raw_input("Please enter the username for Spotify:")
#print username
playlist = raw_input("Please enter the Playlist name for this event:")
#print playlist
genre = raw_input("What type of music would you want for this event?")
#print genre
numSongs = raw_input("How many songs do you want for this")
#print numSongs

spotLoc = state+" , "+state
Spotify.make_playlist(username, playlist, genre, spotLoc, numSongs)

