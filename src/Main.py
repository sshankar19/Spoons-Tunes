import Music
import Spotify
import pyechonest
import sys
import spotipy

username = sys.argv[1]
playlistName = sys.argv[2]
genre = sys.argv[3]
location = sys.argv[4]
numSongs = sys.argv[5]

Spotify.make_playlist(username, playlistName, genre, location, numSongs)
