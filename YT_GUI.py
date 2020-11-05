try:
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
    import sys
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("some modules are missing {}".format(e))
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,70,1000,900)
        self.setWindowTitle("Gui with Aryan")
        self.initUI()
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter URL")
        self.label.move(50,50)
        self.textbox = QLineEdit(self)
        self.textbox.move(200,40)
        self.textbox.resize(280,40)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Enter Download Path")
        self.label1.move(50,150)
        self.label1.resize(150,15)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(200,140)
        self.textbox1.resize(280,40)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Enter resolution (“720p”, “480p”, “360p”, “240p”, “144p”)")
        self.label2.move(50,250)
        self.label2.resize(500,15)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(200,280)
        self.textbox2.resize(280,40)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Download Video")
        self.b1.move(250,400)
        self.b1.resize(280,40)
        self.b1.clicked.connect(self.download_vid)
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Download Playlist")
        self.b2.move(250,450)
        self.b2.resize(280,40)
        self.b2.clicked.connect(self.download_list)
    def download_vid(self):
        url = self.textbox.text()
        path = self.textbox1.text()
        res = self.textbox2.text()
        videos(url,path,res)
    def download_list(self):
        url = self.textbox.text()
        path = self.textbox1.text()
        res = self.textbox2.text()
        videos(url,path,res)

def videos(url,path,res):
    ytd = YouTube(url)
    stream = ytd.streams.filter(progressive=True)
    try:
        file = stream.get_by_resolution(res)
        file.download(path)
        print("File Downloaded successfully")
    except:
        print("File not Downloaded")

def playlist(url,path,res):
    count = 1
    playlist = Playlist(url)
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

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()
