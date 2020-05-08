""" 시도별 발생현황 """

from bs4 import BeautifulSoup
import urllib.request

url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

num = 1

for i in soup.select('button'):
  print(i.select_one('span.name').get_text(), end = ' ')
  print(i.select_one('span.num').get_text(), end = ' ')
  print(i.select_one('span.before').get_text())

print()

for j in soup.select('div.mapview > div.citychart > p'):
  if num <= 5:
    print(j.get_text())
    num += 1