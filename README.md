# Duolingo-spotify-music-learner
Alot of folks use music to learn a language but how do we find music we can use to practice 
the verbs we just learned. This tools goal is to use the recent verbs you learned in duolingo 
and find music that uses those verbs to help learners learn

## Apis needed installed
### DuoLingo api
There is no official duolingo api so what I am using is [duolingo api for python](https://github.com/KartikTalwar/Duolingo#duolingo-api-for-python).
With this though there is a [known issue](https://github.com/KartikTalwar/Duolingo/issues/128) making it unable to login so I installed [this fork](https://github.com/tier61wro/Duolingo) of the package. Or one can simply do a ```pip install duolingo-api``` and change the package themselves.
```commandline
pip install duolingo-api 
# or
pip install git+https://github.com/tier61wro/Duolingo.git
```

### Spotipy api
I am using the official spotify api for python called [spotipy](https://spotipy.readthedocs.io/en/2.22.1/) 
for installing this api the dev will have to run this api call. 
```commandline
pip install spotipy
```

### Genius api 
I am using the official genius api for python [here](https://lyricsgenius.readthedocs.io/en/master/index.html).
one will need to create a genius account and add a file called ```Genius.py``` in the ```/secrets``` folder
to store the token of the application.
```commandline
pip install lyricsgenius
```

