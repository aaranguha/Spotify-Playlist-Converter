import os
import appscript as aps
import subprocess

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
    output_file = input("Enter output file name: ")
    get_playlist_data(playlist_name, output_file + ".txt")
    print("Playlist exported successfully to {}.txt".format(output_file))

if __name__ == '__main__':
    main()
