from pyechonest import config
from pyechonest import artist
from pyechonest import playlist

config.ECHO_NEST_API_KEY = "O5MCJTHFAF7PVI9Q6"

def getArtistsByGenre(genre, maxNum=4):
    """
    Given genre in TODO: genreList/enum?, returns list of artists
    
    Keyword arguments:
    genre -- string 
    maxNum -- 10 by default, maxNumber of artists to return (<50 please)
   
    """
    
    #TODO: assert genre is a valid genre
    
    min_famil = 0.60
    artists = artist.search(style=genre, min_familiarity=min_famil) #Gets list in format [<artist - artistName>]
    artistList = []
    #parse artists into list
    for i in xrange(min(len(artists), maxNum)):
        artistList.append(artists[i].__str__())
    return artistList

#print getArtistsByGenre("classical")

def getArtistsByLocation(location, appID="Spoons-Tunes", maxNum=1):
    """
    Given location, returns list of nearby bands playing
    
    Keyword arguments:
    location -- in format "city,state", "city,country", "lat,lon", "ip address"
    maxNum -- maximum number of artists to return
    """
    
    #TODO: assert location is a valid location
    location.replace(" ", "+")
            
    import urllib2

    response = urllib2.urlopen("http://api.bandsintown.com/events/search.json?location=%s&app_id=%s" %(location, appID)) 
    html = response.read()

    ctr = 0
    
    artistList = []
    while (html.find("\"name\":\"")!= -1) and ctr < maxNum:
        curIndex = html.find("\"name\":\"")
        html = html[curIndex+8:]
        endIndex = html.find("\"")
        str = html[:endIndex]
        try:
            artist.Artist(str)
            ctr+=1
            artistList.append(str)
        except:
            continue

    return artistList

    
#print getArtistsByLocation("New+York, NY")

def genPlaylist(artistList):
    """
    Given list of artists, creates playlist radio
    """

    pList = playlist.Playlist(type="artist-radio", artist=artistList)
    while True:

        yield pList.get_next_songs()
        
def getPlayList(genre, location, numSongs=20):
    """
    Given genre and location, return list of songs
    """
    listTest = getArtistsByGenre(genre) + getArtistsByLocation(location)
    final = genPlaylist(listTest[:5])
    
    ctr = 0
    songList = []
    while ctr < numSongs:
        try:
            nextSong = next(final)
        except:
            return songList
        songList.append(nextSong[0])
        ctr+=1
    return songList
    
#getPlayList("rock", "New+York,NY")
    

# 
# #===============================================================================
# # import spotipy
# # spotify = spotipy.Spotify()
# #===============================================================================
# 
# #results = spotify.search(q='genre:' + genre.replace(" ", "+"), type="track")
# 
# 
# ###################
# 
# 
# 
# def getPlaylist():
#     return
#===============================================================================