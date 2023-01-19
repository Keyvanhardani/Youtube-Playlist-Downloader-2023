import re
from pytube import Playlist
from mhyt import yt_download

# Define the YouTube playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLShsMOdvHK0yzbVhNySAFlpwkXOPx_LfY"

# Compile a regular expression to extract the video URLs from the playlist
video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# Create a Playlist object using the URL
playlist = Playlist(playlist_url)

# Overwrite the default video regex with the one we just defined
playlist._video_regex = video_regex

# Print the number of videos in the playlist
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Iterate through the video URLs
for url in playlist.video_urls:
    # Get the length of the URL
    number = len(url)
    # Iterate through the URL string
    for i in range(0, number ):
        # Download the video using the yt_download function and save it as an mp4 file with incremental number as the file name.
        yt_download(url,"Video-"+str(i)+".mp4")
    


       
