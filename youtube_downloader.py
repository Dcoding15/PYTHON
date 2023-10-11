from pytube import YouTube

getLink = input("Enter YouTube Link: ")
yt = YouTube(getLink)
video = yt.streams.get_highest_resolution()
video.download()
print("!!!Done!!!")