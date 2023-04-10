import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Set up the authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="http://example.com/callback/",
                                               scope="playlist-modify-public"))

# Create the new playlist or get the existing one
playlist_name = "Python"
user_id = sp.me()["id"]
playlists = sp.user_playlists(user=user_id)
existing_playlists = [p for p in playlists["items"] if p["name"] == playlist_name]
if existing_playlists:
    playlist = existing_playlists[0]
else:
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name)
playlist_id = playlist["id"]

# Read the file containing the track names
with open("songs.txt", "r") as file:
    track_names = file.readlines()
    track_names = [name.strip() for name in track_names]

# Add the tracks to the playlist
total_requests = len(track_names)
requests_completed = 0
start_time = time.time()
for name in track_names:
    # Search for the track by name
    results = sp.search(q=name, type="track", limit=1)
    items = results["tracks"]["items"]
    if items:
        track_uri = items[0]["uri"]
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=[track_uri])
    requests_completed += 1
    elapsed_time = time.time() - start_time
    requests_per_second = requests_completed / elapsed_time
    remaining_requests = total_requests - requests_completed
    time_remaining = remaining_requests / requests_per_second
    print(f"Completed {requests_completed}/{total_requests} requests. Estimated time remaining: {time_remaining:.2f} seconds.")
    time.sleep(0.1)  # Add a delay of 0.1 seconds between requests to avoid exceeding rate limit

print("Program is complete. Check your Spotify for the updated playlist.")
