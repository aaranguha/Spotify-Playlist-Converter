import os
import appscript as aps
import subprocess

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
    edit_song_info('songs.txt')


if __name__ == '__main__':
    main()
