from pyicloud import PyiCloudService

# Log in to Apple Music account
api = PyiCloudService('aaranguhaca@gmail.com', '3KYN3IKLaaran')

# Get playlist ID
playlists = api.music.playlists()
playlist_name = 'Playlist Tester'
playlist_id = next((playlist['playlistId'] for playlist in playlists if playlist['name'] == playlist_name), None)

# Get songs in playlist
songs = api.music.playlist_songs(playlist_id)

# Write songs to file
with open('songs.txt', 'w') as f:
    for song in songs:
        f.write(song['name'] + '\n')



#call spotify file
exec(open("playlist_converter.py").read())
