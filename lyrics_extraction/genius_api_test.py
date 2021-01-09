class GetLyrics():
    
    def __init__(self, spotify_client_id, spotify_client_secret, user_id, playlist_id, genius_key):
        self.spotify_client_id = spotify_client_id
        self.spotify_client_secret = spotify_client_secret
        self.user_id = user_id
        self.playlist_id = playlist_id
        self.genius_key = genius_key
        
    def get_playlist_info(self):
        token = SpotifyClientCredentials(client_id=self.spotify_client_id, client_secret=self.spotify_client_secret).get_access_token()
        sp = spotipy.Spotify(token)
        playlist = sp.user_playlist_tracks(self.user_id, self.playlist_id)
        self.playlist = playlist
        return self.playlist
    
    def get_track_names(self):
        track_names = []
        for song in range(len(self.playlist['items'])):
            track_names.append(self.playlist['items'][song]['track']['name'])
        self.track_names = track_names
        return self.track_names
    
    def get_track_artists(self):
        track_artists = []
        for song in range(len(self.playlist['items'])):
            track_artists.append(self.playlist['items'][song]['track']['artists'][0]['name'])
        self.track_artists = track_artists
        return self.track_artists
        
    def request_song_info(self, track_name, track_artist):
        self.track_name = track_name
        self.track_artist = track_artist
        base_url = 'https://api.genius.com'
        headers = {'Authorization': 'Bearer ' + self.genius_key}
        search_url = base_url + '/search'
        data = {'q': track_name + ' ' + track_artist}
        response = requests.get(search_url, data=data, headers=headers)
        self.response = response
        return self.response

    def check_hits(self):
        json = self.response.json()
        remote_song_info = None
        for hit in json['response']['hits']:
            if self.track_artist.lower() in hit['result']['primary_artist']['name'].lower():
                remote_song_info = hit
                break
        self.remote_song_info = remote_song_info
        return self.remote_song_info
    
    def get_url(self):
        song_url = self.remote_song_info['result']['url']
        self.song_url = song_url
        return self.song_url
    
    def scrape_lyrics(self):
        page = requests.get(self.song_url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics1 = html.find("div", class_="lyrics")
        lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
        if lyrics1:
            lyrics = lyrics1.get_text()
        elif lyrics2:
            lyrics = lyrics2.get_text()
        elif lyrics1 == lyrics2 == None:
            lyrics = None
        return lyrics

    def get_lyrics(self):
        playlist = GetLyrics.get_playlist_info(self)
        track_names = GetLyrics.get_track_names(self)
        track_artists = GetLyrics.get_track_artists(self)
        song_lyrics = []
        for i in range(len(self.track_names)):
            print("\n")
            print(f"Working on track {i}.")
            response = GetLyrics.request_song_info(self, self.track_names[i], self.track_artists[i])
            remote_song_info = GetLyrics.check_hits(self)
            if remote_song_info == None:
                lyrics = None
                print(f"Track {i} is not in the Genius database.")
            else:
                url = GetLyrics.get_url(self)
                lyrics = GetLyrics.scrape_lyrics(self)
                if lyrics == None:
                    print(f"Track {i} is not in the Genius database.")
                else:
                    print(f"Retrieved track {i} lyrics!")
            song_lyrics.append(lyrics)
        return song_lyrics

songs = GetLyrics('89e3323f79474b3a9de0caf291ba18de', 'd0a84797538d4c8c86eed735569a24a5', 'qf5jdmz62v8a4uv8bcnsykslr', '6MJR7akK3U2e9awLhYEyO9', 'hVMr77CREdBmeFB0NsGtpvvl7wrcKq5DcN32a3N0YWPtSRAQrbkFIY6XQ4Jfi6fa')
song_lyrics = songs.get_lyrics()