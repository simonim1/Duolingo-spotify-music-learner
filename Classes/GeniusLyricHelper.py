from lyricsgenius import Genius
from Secrets.Genius import TOKEN
class GeniusHelper:
    def __init__(self):
        self.genius = Genius(TOKEN)

    ###################################################
    #                 private functions               #
    ###################################################

    def _get_song_id(self, song_name, artist):
        '''
        :param song_name: String of full song name
        :param artist: String of full artist names
        :return: will return the genius song id the idea that the first
        song we find is the correct one
        '''
        song_list = self.genius.search_songs(song_name, excluded_terms=["(Remix)", "(Live)"])
        for song in song_list:
            if song['type'] == 'song':
                if song['result']['artist_names'] == artist:
                    return song['result']['id']

    def _get_song_lyrics(self, song_id):
        '''
        must call get_song_id to get the songs id
        :param song_id: string of the id
        :return:
        '''
        self.genius.lyrics(song_id)

    ###################################################
    #                 public functions               #
    ###################################################

    def verb_in_song(self, song_name, artist, verb):
        '''
        :param song_name: string of the song name
        :param artist: string of artists name
        :param verb: verb one is searching for in the song, string
        :return: return true if the verb is found else false
        '''
        song_id = self._get_song_id(song_name,artist)
        lyrics = self._get_song_lyrics(song_id)

        if verb in lyrics:
            return True
        return False
