import os
import spotipy
from spotipy.oauth2 import *

#TODO: https://medium.com/swlh/how-to-leverage-spotify-api-genius-lyrics-for-data-science-tasks-in-python-c36cdfb55cf3



class Spotify:
    def __init__(self, client_id, client_secret, redirect_uri):
        '''
        :param client_id: your spotify app client id
               client_secret: your client secret
               redirect_uri: is the redirect URL for your application
        you get all of this once you make an app on spotify's dev page
        https://developer.spotify.com/documentation/web-api
        '''
        scope = "user-library-read playlist-read-private"
        self.spotipyClientId = client_id
        self.spotipyClientSecret = client_secret
        self.spotipyRedirect_uri = redirect_uri
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_secret=self.spotipyClientSecret,
                                                       client_id=self.spotipyClientId,
                                                       redirect_uri=self.spotipyRedirect_uri,
                                                       scope=scope))





