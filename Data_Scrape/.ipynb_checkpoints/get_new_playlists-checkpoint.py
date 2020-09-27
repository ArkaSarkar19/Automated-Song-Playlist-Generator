import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f053486a0d364fe09c5bddf49fc4657e",
                                                           client_secret="701cacd9264046d7889ab46f6f7610a9"))
f = open("Playlist_properties/playlist_names.txt" ,"r")

f = open("Playlist_properties/playlist_names.txt" ,"r")
dict_ = open("Pickle_Files/Msd_id_to_spotify_id.pkl", "rb")
dict_ = pickle.load(dict_)
dict_ = dict(map(reversed, dict_.items()))

playlist_list = []
bias = 0
for i in range(10):
	results = sp.search(q="latin", type='playlist', limit = 50, offset = bias)
	bias += 50
	for j in range(len(results['playlists']['items'])):
		playlist_id = results['playlists']['items'][j]['id']
		playlist_list.append(playlist_id)

s = set()
for c in playlist_list:
	s.add(c)

playlist_list = list(s)

print(len(playlist_list))


for playlist_id in playlist_list:		
	offset = 0
	count = 0
	while(1):
		results1 = sp.playlist_items(playlist_id, offset = offset, limit = 100)
		if(len(results1['items']) == 0):
			break
		for j in range(len(results1['items'])):
			try:
				song_id = results1['items'][j]['track']['id']
				if(song_id in dict_):
					count+=1
			except:
				continue
		offset += len(results1['items'])
	
# 	# print(results['playlists']['items'][i]['name'])
	if count > 50:
		print(playlist_id, count,offset)

