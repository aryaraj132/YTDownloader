import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import os
from pytube import YouTube
from pytube import Playlist



class MyGrid(Widget):
    url = ObjectProperty(None)
    path = ObjectProperty(None)
    res = ObjectProperty(None)

    def btn1(self):
        MyApp.videos(self,self.url.text, self.path.text, self.res.text)
    def btn2(self):
        MyApp.playlist(self,self.url.text, self.path.text, self.res.text)




class MyApp(App):
    def build(self):
        return MyGrid()
    Dir = os.path.dirname(os.path.realpath(__file__))
    def videos(self,url,path,res):
        try:
            ytd = YouTube(url)
            stream = ytd.streams.filter(progressive=True)
            file = stream.get_by_resolution(res)
            file.download(path)
            print('success')
            self.info.text = "File Downloaded"
        except:
            #self.label3.setText("File Not downloaded")
            print('error')
            self.info.text = "File Not Downloaded"
    def playlist(self,url,path,res):
        count = 1
        error = 1
        playlist = Playlist(url)
        for video_url in playlist.video_urls:
            while(True):
                try:
                    ytd = YouTube(video_url)
                    stream = ytd.streams.filter(progressive=True)
                    file = stream.get_by_resolution(res)
                    file.download(path + '\\' + playlist.title())
                    self.info.text = str(count) + "File Downloaded"
                    count+=1
                    break
                except:
                    self.info.text = str(error) + "File Not Downloaded"
                    error+=1
                    break

if(__name__ == "__main__"):
    MyApp().run()


def videos(url,path,res):
    ytd = YouTube(url)
    stream = ytd.streams.filter(progressive=True)
    try:
        file = stream.get_by_resolution(res)
        file.download(path)
        #self.label3.setText("File downloaded")
    except:
        #self.label3.setText("File Not downloaded")
        print('error')



