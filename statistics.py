from bs4 import BeautifulSoup
import urllib.request

""" 코로나 통계 """

url = 'http://ncov.mohw.go.kr/index.jsp'

header = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# urllib.error.HTTPError: HTTP Error 403: Forbidden 오류 뜨면 위 코드를 넣어주어야 함

html = urllib.request.urlopen(header).read()
soup = BeautifulSoup(html, 'html.parser')

title = []
sta = []

for statistics in soup.select('ul.liveNum > li > strong'):
  title.append(statistics.get_text())
  
for statistics in soup.select('ul.liveNum > li > span'):
  sta.append(statistics.get_text())

i = 0

while(i < len(sta)):

  if(i % 2 == 0):
    print(title[int(i / 2)])
    print(sta[i], sta[i + 1], '\n')

  i = i + 1