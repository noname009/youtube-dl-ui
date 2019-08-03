import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

fileserch = os.listdir(os.path.dirname(os.path.abspath(__file__)))
if 'youtube-dl.exe' in fileserch:
    pass
else:
    os.system(os.path.dirname(os.path.abspath(__file__)) + '/install.exe')

form_class = uic.loadUiType("untitled.ui")[0]
defaultpath = os.path.dirname(os.path.abspath(__file__)) + '/download'
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_Print.clicked.connect(self.appendTextFunction)
        self.pushButton.clicked.connect(self.showDialog)
        self.pushButton_2.clicked.connect(self.updatecheck)

    def showDialog(self):
        global defaultpath
        defaultpath = QFileDialog.getExistingDirectory(self, 'select Directory')
        self.pushButton.setText(defaultpath)
        
    def appendTextFunction(self) :
        youcho = self.comboBox.currentText()
        url = self.lineEdit.text()
        if youcho == 'Default':
            result = os.system('youtube-dl.exe -i -o "{}/%(title)s.%(ext)s" {}'.format(defaultpath, url))
            if result == 1:
                self.textbrow_Test.append('[다운로드 실패]')
            else:
                self.textbrow_Test.append('[Default 다운로드 성공]')
        if youcho == 'MP3':
            result = os.system('youtube-dl --extract-audio --audio-format mp3 -i -o "{}/%(title)s.%(ext)s" {}'.format(defaultpath, url))
            if result == 1:
                self.textbrow_Test.append('[다운로드 실패]')
            else:
                self.textbrow_Test.append('[MP3 다운로드 성공]')
        if youcho == 'BEST':
            result = os.system('youtube-dl -f best -i -o "{}/%(title)s.%(ext)s" {}'.format(defaultpath, url))
            if result == 1:
                self.textbrow_Test.append('[다운로드 실패]')
            else:
                self.textbrow_Test.append('[BEST 다운로드 성공]')
    def updatecheck(self) :
        try:
            url = 'https://ytdl-org.github.io/youtube-dl/download.html'
            html = urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            vurl = soup.find_all('a')[2]['href']
            with open(os.path.dirname(os.path.abspath(__file__)) + '/version.txt', 'r') as file :
                versiondata = file.read()
            if versiondata == vurl.split('/')[4]:
                self.textbrow_Test.append('[최신버전입니다]')
            else:
                self.textbrow_Test.append('[업데이트 시작]')
                with open(os.path.dirname(os.path.abspath(__file__)) + '/youtube-dl.exe', "wb") as file:
                    response = urlopen(vurl).read()
                    file.write(response)
                with open(os.path.dirname(os.path.abspath(__file__)) + '/version.txt', 'w') as file :
                    file.write(vurl.split('/')[4])
                self.textbrow_Test.append('[업데이트 완료]')
        except:
            self.textbrow_Test.append('[업데이트 실패 - 나중에 다시 시도해주세요]')
               
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
