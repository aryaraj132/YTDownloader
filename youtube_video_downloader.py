# -*- coding: utf-8 -*-
"""
@author: Aryan Raj
"""
try:
    from pytube import YouTube
except Exception as e:
    print("some modules are missing {}".format(e))

url = "https://youtu.be/m_7JMmBW-Zc"
path = 'C:/Users/aryar/Downloads/'
ytd = YouTube(url)
stream = ytd.streams.filter(progressive=True)
#stream_audio = ytd.streams.filter(only_audio=True)
#pt.extract.apply_descrambler(stream, 'Stream')
#print(stream)
print('Type exit to end program')
while True:
    try: 
        res = input("Enter resolution (“720p”, “480p”, “360p”, “240p”, “144p”) : ")
        if res == 'exit':
            break
        file = stream.get_by_resolution(res)
        file.download(path)
        print("File Downloaded successfully")
        break
    except:
        print("This resolution is not available try again")
