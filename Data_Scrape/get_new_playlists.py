import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="89e3323f79474b3a9de0caf291ba18de",
                                                           client_secret="d0a84797538d4c8c86eed735569a24a5"))
f = open("playlist_names.txt" ,"r")

f = open("playlist_names.txt" ,"r")
dict_ = open("Msd_id_to_spotify_id.pkl", "rb")
dict_ = pickle.load(dict_)
dict_ = dict(map(reversed, dict_.items()))

playlist_list = []
bias = 0
for i in range(10):
	results = sp.search(q="summer", type='playlist', limit = 50, offset = bias)
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
		print(results['playlists']['items'][i]['name'], playlist_id, count,offset)

