from lyricsgenius import Genius

class GeniusHelper:
    def __init__(self, token):
        self.genius = Genius(token,excluded_terms=["(Remix)", "(Live)"])

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
        song_list = self.genius.search_songs(song_name)
        if song_name == 'Bendita Tu Luz': # this is a bug it is on the genius site but cant seem to find this song
            print(song_list)
        for song in song_list['hits']:
            if song_name == 'Bendita Tu Luz':
                print('********************************')
                print(song)
                print('********************************')
            if song['type'] == 'song':
                if song['result']['artist_names'] == artist:
                    return song['result']['id']

    def _get_song_lyrics(self, song_id):
        '''
        must call get_song_id to get the songs id
        :param song_id: string of the id
        :return:
        '''
        return self.genius.lyrics(song_id)

    ###################################################
    #                 public functions               #
    ###################################################

    def verb_in_song(self, song_name, artist, verbs):
        '''
        :param song_name: string of the song name
        :param artist: string of artists name
        :param verb: verb one is searching for in the song, string
        :return: return true if the verb is found else false
        '''
        song_id = self._get_song_id(song_name,artist)
        if song_id != None:
            lyrics = self._get_song_lyrics(song_id)
            for verb in verbs:
                if verb in lyrics:
                    return True
                return False
