import Music
import sys
import spotipy
import spotipy.util as util
import urllib

def make_playlist(username="stellamplau", playlistName="Spoons&Tunes", genre="rock", location="Boston,MA", numSongs=30):
    scope = 'playlist-modify-private'

    token = util.prompt_for_user_token(username, scope,"2a1cd7b9a1ee4294b4085e52d2ac51a2", "e771e11a11f9444c906f6eccabf3a037","http://google.com")
    songList =  Music.getPlayList("rock", "Boston,MA", 30)
    spotify = spotipy.Spotify(auth=token)
    curlist = spotify.user_playlist_create(username,playlistName, public=False)
    
    songIDs = []
    
    for song in songList:
        
        #print song
        songDict = song.get_tracks('spotify-WW')[0]
        id = songDict['foreign_id']
        songIDs.append(id[14:])
        
    
    #print songIDs
    #print curlist['id']
    
    spotify.user_playlist_add_tracks(username, curlist['id'], songIDs)





