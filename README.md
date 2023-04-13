#Spotify Playlist Creator
This program allows you to export a playlist from Apple Music and create a new playlist in Spotify with the same songs.

Dependencies
os
appscript
subprocess
spotipy
time
You can install the dependencies using pip:

bash
Copy code
pip install appscript spotipy
Usage
To use this program, you must have both an Apple Music and Spotify account.

Open the spotify_playlist_creator.py file in a code editor.
Edit the client_id, client_secret, and redirect_uri values in the SpotifyOAuth call with your own values.
Run the program in the terminal by typing python spotify_playlist_creator.py and pressing enter.
Enter the name of the Apple Music playlist you want to export when prompted.
Wait for the program to finish running. The new Spotify playlist will be created and the songs will be added to it.
Functions
spotify_playlist_creator(playlist_name: str, file_path: str): This function creates a new Spotify playlist with the given name and adds the tracks from the given file path to the playlist. If a playlist with the given name already exists, it will add the tracks to that playlist instead.
edit_song_info(file_path): This function edits the song information in the file at the given file path. It expects the file to be in CSV format with the following columns: song ID, song name, artist name, album name, and song duration. It converts each row to a string in the format "song name - artist name" and writes the new strings to the same file.
get_playlist_data(playlist_name, output_file): This function exports the tracks from the given Apple Music playlist to a text file. It uses AppleScript to interact with the Music app and retrieve the track information.
main(): This function runs the main logic of the program. It prompts the user to enter the name of the Apple Music playlist they want to export, exports the playlist to a text file, edits the song information in the text file, and creates a new Spotify playlist with the edited songs.
Disclaimer
This program is intended for educational purposes only. Use at your own risk. The author is not responsible for any damage or loss of data caused by this program.