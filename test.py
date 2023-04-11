import os
import appscript as aps
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Set up the authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="889aea68732540fcb8f5ad3e672f548f",
                                               client_secret="secret key, can't be displayed for security reasons",
                                               redirect_uri="http://example.com/callback/",
                                               scope="playlist-modify-public"))


def spotify_playlist_creator(playlist_name: str, file_path: str):
    # Get user ID
    user_id = sp.me()["id"]

    # Get list of user's playlists
    playlists = sp.user_playlists(user=user_id)

    # Check if playlist with given name already exists
    existing_playlists = [p for p in playlists["items"] if p["name"] == playlist_name]

    # If playlist exists, use the first one in the list
    if existing_playlists:
        playlist = existing_playlists[0]
    # If playlist does not exist, create a new one with the given name
    else:
        playlist = sp.user_playlist_create(user=user_id, name=playlist_name)

    # Get the playlist ID
    playlist_id = playlist["id"]

    # Read the file containing the track names
    with open(file_path, "r") as file:
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

def edit_song_info(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            line = line.strip()
            parts = line.split(',')
            if len(parts) >= 3:
                song_name = parts[1]
                artist_name = parts[2]
                new_line = "{} - {}\n".format(song_name, artist_name)
                file.write(new_line)

def get_playlist_data(playlist_name, output_file):
    script = '''
        tell application "Music"
            set myPlaylist to first playlist whose name is "{0}"
            set myTracks to tracks of myPlaylist
            set myData to ""
            repeat with myTrack in myTracks
                set myData to myData & (id of myTrack as string) & ","
                set myData to myData & (name of myTrack as string) & ","
                set myData to myData & (artist of myTrack as string) & ","
                set myData to myData & (album of myTrack as string) & ","
                set myData to myData & (duration of myTrack as integer) & "\\n"
            end repeat
        end tell
        return myData
    '''
    # Use subprocess to run osascript command and capture output
    output = subprocess.check_output(['osascript', '-e', script.format(playlist_name)], text=True)
    with open(output_file, 'w') as file:
        file.write(output)
def main():
    playlist_name = input("Enter playlist name: ")
    output_file = "songs"
    get_playlist_data(playlist_name, output_file + ".txt")
    print("Playlist exported successfully to {}.txt".format(output_file))
    print("Creating New Playlist in Spotify and adding songs...")

    edit_song_info('songs.txt')
    spotify_playlist_creator(playlist_name, "songs.txt")


if __name__ == '__main__':
    main()
