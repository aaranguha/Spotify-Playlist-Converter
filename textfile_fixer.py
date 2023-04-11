with open('songs.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(',')
        song_name = parts[1]
        artist_name = parts[2]
        print("Song: {}, Artist: {}".format(song_name, artist_name))