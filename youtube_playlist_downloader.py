try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("some modules are missing {}".format(e))
count = 1
url = input("Enter URL to download : ")
path = input("Enter Path to download to : ")
playlist = Playlist(url)
res = input("Enter resolution (“720p”, “480p”, “360p”, “240p”, “144p”) : ")
for video_url in playlist.video_urls:
    try:
        ytd = YouTube(video_url)
        stream = ytd.streams.filter(progressive=True)
        file = stream.get_by_resolution(res)
        file.download(path)
        print("{} File Downloaded successfully".format(count))
        count+=1
    except:
        print("error found please provide proper resolution ")
        break