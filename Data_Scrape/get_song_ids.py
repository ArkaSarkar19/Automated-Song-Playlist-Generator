import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f053486a0d364fe09c5bddf49fc4657e",
                                                           client_secret="701cacd9264046d7889ab46f6f7610a9"))
f = open("Playlist_properties/playlist_ids.txt" ,"r")

playlist_list = []
for line in f:
	playlist_id, x, y = line.split() 
	playlist_list.append(playlist_id)
f.close()

f = open("Playlist_properties/playlist_names.txt" ,"r")
dict_ = open("Pickle_Files/Msd_id_to_spotify_id.pkl", "rb")
dict_ = pickle.load(dict_)
dict_ = dict(map(reversed, dict_.items()))
f.close()

song_ids = set()

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
					song_ids.add(song_id)
			except:
				continue
		offset += len(results1['items'])
	print(playlist_id, count,offset)

list1 = list(song_ids)
print(list1)
print(len(list1))

f = open("Pickle_Files/relevant_songs.pkl", "wb")
pickle.dump(list1, f)
f.close()
	
# # 	# print(results['playlists']['items'][i]['name'])
# 	if count > 50:
		# print(playlist_id, count,offset)

