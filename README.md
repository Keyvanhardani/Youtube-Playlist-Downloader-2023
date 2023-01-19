# Youtube-Playlist-Downloader-2023
Download whole Playlist from Youtube

This script is using the "re" and "pytube" python libraries to access and download videos from a specific YouTube playlist. It starts by defining the YouTube playlist URL and uses a regular expression to extract the video URLs from the playlist. Then it creates a Playlist object using the URL and overwrites the default video regex with the one we just defined. Next, it prints the number of videos in the playlist. Finally, it uses a for loop to iterate through the video URLs, and for each video, it uses the "yt_download" function from the "mhyt" library to download the video and save it as an mp4 file with an incremental number as the file name.

Thanks to ChatGPT, for writing the comments and description for this code.
