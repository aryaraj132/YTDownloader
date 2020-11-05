try:
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
    import sys
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("some modules are missing {}".format(e))

def setvalue(str,str1):
    url = str
    path = str1
    print(url, path)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,70,1000,900)
    win.setWindowTitle("Gui with Aryan")
    label = QtWidgets.QLabel(win)
    label.setText("Enter URL")
    label.move(50,50)
    textbox = QLineEdit(win)
    textbox.move(200,40)
    textbox.resize(280,40)
    label1 = QtWidgets.QLabel(win)
    label1.setText("Enter Download Path")
    label1.move(50,150)
    label1.resize(150,15)
    textbox1 = QLineEdit(win)
    textbox1.move(200,140)
    textbox1.resize(280,40)
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Submit")
    b1.move(200,250)
    b1.clicked.connect(setvalue(textbox.text(), textbox1.text()))
    label2 = QtWidgets.QLabel(win)
    label2.setText("Enter resolution (“720p”, “480p”, “360p”, “240p”, “144p”)")
    label2.move(50,350)
    label2.resize(500,15)
    win.show()
    sys.exit(app.exec_())
window()