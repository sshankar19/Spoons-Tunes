import Music
import sys
import spotipy
import spotipy.util as util
import pyechonest


authURL = "https://accounts.spotify.com/authorize?scope=playlist-modify-private&redirect_uri=http%3A%2F%2Fgoogle.com&response_type=code&client_id=2a1cd7b9a1ee4294b4085e52d2ac51a2"


def make_playlist(username, playlistName="Spoons&Tunes", genre="rock", location="Boston,MA", numSongs=20):
    scope = 'playlist-modify-private'

    token = util.prompt_for_user_token(username, scope,"2a1cd7b9a1ee4294b4085e52d2ac51a2", "e771e11a11f9444c906f6eccabf3a037","http://google.com")
    songList =  Music.getPlayList(genre, location, numSongs)
    spotify = spotipy.Spotify(auth=token)
    curlist = spotify.user_playlist_create(username,playlistName, public=False)
    
    songIDs = []
    
    for song in songList:
        
        #print song
        
        songDict = spotify.search(q='track:'+song.__str__(),limit=1,type='track')
        for i, t in enumerate(songDict['tracks']['items']):
            songIDs.append( t['external_urls']['spotify'])
            break

        #songDict = song.get_tracks('spotify-WW')[0]
        #id = songDict['foreign_id']
        #songIDs.append(id[14:])
        
    #print len(songIDs)
   # print curlist['id']
    
    spotify.user_playlist_add_tracks(username, curlist['id'], songIDs)
