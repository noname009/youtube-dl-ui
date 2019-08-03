import os
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
import platform

version = os.path.dirname(os.path.abspath(__file__)) + '/version.txt'
url = 'https://ytdl-org.github.io/youtube-dl/download.html'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
vurl = soup.find_all('a')[2]['href']
print('youtube-dl 다운로드 시작...')
with open(os.path.dirname(os.path.abspath(__file__)) + '/youtube-dl.exe', "wb") as file:
    response = urlopen(vurl).read()
    file.write(response)
print('youtube-dl 다운로드 완료...')
print('ffmpeg 복사 시작...')
with open(os.path.dirname(os.path.abspath(__file__)) + '/version.txt', 'w') as file :
    file.write(vurl.split('/')[4])
if platform.machine().endswith('64'):
    shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + '/ffmpeg/64-bin/ffmpeg.exe', os.path.dirname(os.path.abspath(__file__)) + '/ffmpeg.exe')
    print('64비트 적용')
else:
    shutil.copy2(os.path.dirname(os.path.abspath(__file__)) + '/ffmpeg/32-bin/ffmpeg.exe', os.path.dirname(os.path.abspath(__file__)) + '/ffmpeg.exe')
    print('32비트 적용')
input('[설정 완료]\n아무 키나 눌러서 종료...')
