import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f053486a0d364fe09c5bddf49fc4657e",
                                                           client_secret="701cacd9264046d7889ab46f6f7610a9"))


f = open("song_name_song_artist.pkl" , "rb")
list1 = pickle.load(f)
f.close()

dict1 = {}
for i in range(80000):
	# print(i)
	if(i%100 == 0) :
		print(i)
	try:
		c = list1[i]
		query = c[0] + " " + c[1]
		msd_id = c[2]
		results = sp.search(q=query, limit=1)
		for idx, track in enumerate(results['tracks']['items']):
			dict1[msd_id] = track['id']
	except:
		print("ERROR")

# print(dict1)
f = open("Msd_id_to_spotify_id_0-80000", "wb")
pickle.dump(dict1, f)
f.close()

# print(dict1)