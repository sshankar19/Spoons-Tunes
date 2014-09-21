import Spotify
#import Food
import sys


location = sys.argv[1]
city = sys.argv[2]
state = sys.argv[3]
zipcode = sys.argv[4]
username = sys.argv[5]
playlistName = sys.argv[6]
genre = sys.argv[7]
numSongs = int(sys.argv[8])

assert numSongs < 100

Spotify.make_playlist(username, playlistName, genre, city + "," + state, numSongs)
#Food.getFood(genre, location, city, state, 3.28)



