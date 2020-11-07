import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import os
from pytube import YouTube
from pytube import Playlist



class MyWindow(FloatLayout):
    url = ObjectProperty(None)
    path = ObjectProperty(None)
    res = ObjectProperty(None)
    def on_touch_down(self, touch):
        return super().on_touch_down(touch)
    def on_touch_up(self, touch):
        return super().on_touch_up(touch)


class MyApp(App):
    def build(self):
        return MyWindow()
    Dir = os.path.dirname(os.path.realpath(__file__))
    def videos(self,url,path,res,info):
        try:
            ytd = YouTube(url)
            stream = ytd.streams.filter(progressive=True)
            file = stream.get_by_resolution(res)
            file.download(path)
            info.text = "File Downloaded"
        except:
            info.text = "File Not Downloaded"
    def playlist(self,url,path,res,info):
        count = 1
        error = 1
        try:
            playlist = Playlist(url)
            for video_url in playlist.video_urls:
                while(True):
                    try:
                        ytd = YouTube(video_url)
                        stream = ytd.streams.filter(progressive=True)
                        file = stream.get_by_resolution(res)
                        file.download(path + '\\' + playlist.title())
                        info.text = str(count) + "File Downloaded"
                        count+=1
                        break
                    except:
                        info.text = str(error) + "File Not Downloaded"
                        error+=1
                        break
        except:
            info.text = "File Not Downloaded"

if(__name__ == "__main__"):
    MyApp().run()
