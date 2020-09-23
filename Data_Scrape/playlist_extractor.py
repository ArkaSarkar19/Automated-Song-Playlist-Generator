import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="89e3323f79474b3a9de0caf291ba18de",
                                                           client_secret="d0a84797538d4c8c86eed735569a24a5"))
f = open("playlist_names.txt" ,"r")

links_list1 = []
for line in f:
	playlist_name = line[:-1]
	# print(playlist_name)

	results = sp.search(q=playlist_name, type='playlist', limit = 1)
	links_list1.append((results['playlists']['items'][0]['name'], results['playlists']['items'][0]['external_urls']['spotify']))
	# print(results['playlists']['items'][0]['name'], results['playlists']['items'][0]['external_urls']['spotify'])

links_list2 = []
f = open("All_playlists_spotify_links.txt", "r")
for line in f:
	line = line[:-1]
	question_mark = line.find('?')
	
	if question_mark != -1:
		prefix = line[:question_mark]
	else:
		prefix = line
	links_list2.append(prefix)
	# print(prefix)

# print(links_list1)
# print("\n\n")
# print(links_list2)
print(len(links_list1), len(links_list2))

for i in range(len(links_list1)):
	# print(links_list1[i][1], links_list2[i])
	if links_list1[i][1].find(links_list2[i]) == -1:
		print(links_list1[i][0], links_list1[i][1])
		# print(links_list1[i][0])






