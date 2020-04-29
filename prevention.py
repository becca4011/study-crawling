""" 코로나 예방수칙 """

from bs4 import BeautifulSoup
import urllib.request

url = 'http://ncov.mohw.go.kr/guidelineView.do?brdId=6&brdGubun=61&dataGubun=&ncvContSeq=1996&contSeq=1996&board_id=&gubun='

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

#imgUrl = []
n = 0

for img in soup.find_all('img'):
  #imgUrl.append(img.get('src'))
  urllib.request.urlretrieve('http://ncov.mohw.go.kr' + img.get('src'), './crawling/예방수칙' + str(n + 1) +'.png')
  n += 1