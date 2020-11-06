# -*- coding: utf-8 -*-
"""
@author: Aryan Raj
"""
try:
    from pytube import YouTube
    from pytube import Playlist
    import os
except Exception as e:
    print("some modules are missing {}".format(e))
Dir = os.path.dirname(os.path.realpath(__file__))
count = 1
error = 1
url = input("Enter URL to download : ")
path = Dir
playlist = Playlist(url)
res = input("Enter resolution (“720p”, “480p”, “360p”, “240p”, “144p”) : ")
for video_url in playlist.video_urls:
    while(True):
        try:
            ytd = YouTube(video_url)
            stream = ytd.streams.filter(progressive=True)
            file = stream.get_by_resolution(res)
            file.download(path)
            print("{} File Downloaded successfully".format(count))
            count+=1
            break
        except:
            print("{} File Not downloaded".format(error))
            error+=1
            break