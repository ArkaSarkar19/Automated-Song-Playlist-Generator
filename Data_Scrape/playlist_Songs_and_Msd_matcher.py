import spotipy 
import os
import pickle
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="89e3323f79474b3a9de0caf291ba18de",
                                                           client_secret="d0a84797538d4c8c86eed735569a24a5"))
f = open("Playlist_properties/playlist_names.txt" ,"r")
dict_ = open("Pickle_Files/Msd_id_to_spotify_id.pkl", "rb")
dict_ = pickle.load(dict_)
dict_ = dict(map(reversed, dict_.items()))

print(len(dict_))
links_list1 = []

error = []
count  = 0
for line in f:
	playlist_name = line[:-1]
	results = sp.search(q=playlist_name, type='playlist', limit = 1)
	try :
		playlist_id = results['playlists']['items'][0]['id']
		offset = 0
		while(1):
			results = sp.playlist_items(playlist_id, offset = offset, limit = 100)
			# if(i == 1):
				# break
			# print(results['items'][0]['track']['id'])
			if(len(results['items']) == 0):
				count = 0
				break
			for i in range(len(results['items'])):
				# print(results['items'][i]['track']['id'], end = " ")

				song_id = results['items'][i]['track']['id']
				# print(song_id, end = " ")
				if(song_id in dict_):
					count+=1
			print(playlist_name, count,len(results['items']) )

			offset += len(results['items'])
			count = 0
		offset = 0
	# print("\n\n")
	except:
		# print("Error ")
		# print(playlist_name)
		error.append(playlist_name)
print(error)