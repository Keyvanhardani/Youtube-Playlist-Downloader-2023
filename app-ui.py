import tkinter as tk
import re
from pytube import Playlist
from mhyt import yt_download
import random
import time

def download_videos():
    # Get the value of the playlist URL from the textfield
    playlist_url = playlist_url_entry.get()
    
    # Compile a regular expression to extract the video URLs from the playlist
    video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    
    # Create a Playlist object using the URL
    playlist = Playlist(playlist_url)
    
    # Overwrite the default video regex with the one we just defined
    playlist._video_regex = video_regex
    
    # Print the number of videos in the playlist
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    
    # Update the label to display the number of videos
    video_count_label.config(text=f'Number of videos in the playlist: {len(playlist.video_urls)}')
    
    # Iterate through the video URLs
    for url in playlist.video_urls:
        
        # Set the filename
        filename = "Video-{}-{}.mp4".format(int(time.time()), random.randint(0,10000))
        
        # Download the video using the yt_download function and save it as an mp4 file with incremental number as the file name.
        yt_download(url, filename)

# Create the main window
root = tk.Tk()
root.geometry("600x800")
root.title("YouTube Playlist Downloader")

# Create a label for the playlist URL
playlist_url_label = tk.Label(root, text="Playlist URL:")
playlist_url_label.pack()

# Create a textfield for the playlist URL
playlist_url_entry = tk.Entry(root)
playlist_url_entry.pack()

# Create a download button
download_button = tk.Button(root, text="Download", command=download_videos)
download_button.pack()

# Create a label to display the number of videos in the playlist
video_count_label = tk.Label(root)
video_count_label.pack()

# Run the main loop
root.mainloop()