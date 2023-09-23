#!/usr/bin/python
import os
import time
from simple_term_menu import TerminalMenu
from flask import Flask, request, url_for, session, redirect, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# internal classes
from Classes.duolingoHelper import Duo
from Classes.GeniusLyricHelper import GeniusHelper


# importing secrets
from Classes.Secrets.Genius import TOKEN
from Classes.Secrets.duolingo import DUO_USERNAME, DUO_PASSWORD
from Classes.Secrets.Globals import SPOTIPY_CLIENT_SECRET, SPOTIPY_CLIENT_ID, SPOTIPY_REDIRECT_URI

# Consants
LANGUAGE_LIST = ['Spanish']
PIC_FOLDER = os.path.join('static', 'images')
PLAYLIST_ID = '37i9dQZF1DX6ThddIjWuGT' # soon to remove constants

############################################
#                 Flask                    #
############################################
app = Flask(__name__)

# set the name of the session cookie
app.config['SESSION_COOKIE_NAME'] ='Spotify Cookie'
app.config['UPLOAD_FOLDER'] = PIC_FOLDER

# set a random secret key to sign the cookie
app.secret_key = 'YOUR_SECRET_KEY'

# set the key for the token info in the session dictionary
TOKEN_INFO = 'token_info'

# route to handle logging in
@app.route('/')
def login():
    # create a SpotifyOAuth instance and get the authorization URL
    auth_url = create_spotify_oauth().get_authorize_url()
    # redirect the user to the authorization URL
    return redirect(auth_url)

# route to handle the redirect URI after authorization
@app.route('/redirect')
def redirect_page():
    # clear the session
    session.clear()
    # get the authorization code from the request parameters
    code = request.args.get('code')
    # exchange the authorization code for an access token and refresh token
    token_info = create_spotify_oauth().get_access_token(code)
    # save the token info in the session
    session[TOKEN_INFO] = token_info
    # redirect the user to the save_discover_weekly route
    return redirect(url_for('get_duolingo_verbs',_external=True))

@app.route('/duolingo_verbs')
def get_duolingo_verbs():
    try:
        # get the token info from the session
        token_info = get_token()
    except:
        # if the token info is not found, redirect the user to the login route
        print('User not logged in')
        return redirect("/")

    # Api helpers
    Duolingo = Duo(DUO_USERNAME, DUO_PASSWORD)
    Genius = GeniusHelper(TOKEN)
    spotify  = spotipy.Spotify(auth=token_info['access_token'])


    # workflow
    verbs = Duolingo.get_learned_verbs('Spanish')  # find a way to not hardcode this

    selected_verb = verbs['conocer']  # Make this a selection

    song_list = spotify.playlist_items(PLAYLIST_ID)['items']
    song_artists_list = []  # list of tuples (song_name,Artists)
    for song in song_list:
        song_artist_tup = (song["track"]['name'],song["track"]['artists'][0]['name'])
        song_artists_list.append(song_artist_tup)

    # searching songs that have the verb
    returned_songs = []
    for song in song_artists_list:
        name = song[0]
        artist = song[1]
        if Genius.verb_in_song(song_name=name,artist=artist,verbs=selected_verb):
            returned_songs.append(song)

    duo1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Duo_Headphones_Gray.png')

    return render_template('index.html', duo1=duo1, verbs=song_artists_list)

############################################
#                 helpers                  #
############################################
# function to get the token info from the session
def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        # if the token info is not found, redirect the user to the login route
        redirect(url_for('login', _external=False))

    # check if the token is expired and refresh it if necessary
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if (is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = SPOTIPY_CLIENT_ID,
        client_secret = SPOTIPY_CLIENT_SECRET,
        redirect_uri = url_for('redirect_page', _external=True),
        scope='user-library-read playlist-modify-public playlist-modify-private'
    )

app.run(debug=True)





