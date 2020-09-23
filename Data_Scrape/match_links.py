


f = open("All_playlists_spotify_links.txt", "r")
for line in f:
	line = line[:-1]
	question_mark = line.find('?')
	
	if question_mark != -1:
		prefix = line[:question_mark]
	else:
		prefix = line
	print(prefix)

