from pytube import YouTube
import os
from pathlib import Path


url = YouTube('')

print("downloading....")

video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print("Downloaded! :)")
