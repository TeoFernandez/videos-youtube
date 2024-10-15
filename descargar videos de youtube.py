from pytube import YouTube

url = "" #ingrese la url del video

mi_video = YouTube(url)

mi_video = mi_video.streams.get_highest_resolution()

mi_video.download()