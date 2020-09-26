import os
import pickle
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f053486a0d364fe09c5bddf49fc4657e",
                                                           client_secret="701cacd9264046d7889ab46f6f7610a9"))
f = open("relevant_songs.pkl", "rb")

song_ids = pickle.load(f)
features = ['sp_song_id','danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness','liveness','valence','tempo', 'duration_ms']

unlabelled_song_features = []
for song_id  in song_ids:

	list_ = []
	results1 = sp.audio_features(song_id)
	results2 = sp.track(song_id)
	print(results2)
	list_.append(song_id)
	for feature in features:
		if(feature!="sp_song_id"):
			list_.append(results1[0][feature])

	list_.append(results2['album']['release_date'])
	list_.append(results2['popularity'])

	unlabelled_song_features.append(list_)

	if(len(unlabelled_song_features)%100 == 0):
		print(len(unlabelled_song_features))

df = pd.DataFrame(unlabelled_song_features, columns = ['sp_song_id','danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness','liveness','valence','tempo', 'duration_ms','release_date', 'popularity']) 
df.to_csv("Dataset/unlabelled_song_features.csv", index = False)
print(df.head())