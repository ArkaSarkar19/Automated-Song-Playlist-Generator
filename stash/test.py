import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="89e3323f79474b3a9de0caf291ba18de",
                                                           client_secret="d0a84797538d4c8c86eed735569a24a5"))

results = sp.search(q='7 rings', limit=1)
for idx, track in enumerate(results['tracks']['items']):
	results1 = sp.audio_features(track['id'])	
	print(results1)
	print(track['popularity'])
	# print(track['album'])
	print(track['album']['release_date'])


	# print(idx, track['id'])