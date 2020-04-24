""" 코로나 통계 """

from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')
soup = BeautifulSoup(html, 'html.parser')

statistics = []
title = ['확진환자', '격리해제', '격리중', '사망']
country = ['중국', '아시아(중국 제외)', '유럽', '미주', '아프리카', '호주', '검역단계', '지역사회', '내국인', '외국인']
n = 0
c = 0

for i in soup.select('div.data_table.mgt16 > table.num > tbody > tr > td'):
  statistics.append(i.text)


print('<누적 확진자 현황>\n')

while(n < len(statistics)):
  if (n < 4):
    print(title[n], ':', statistics[n])

  elif (n > 5 and n < 36):
    if (n == 6):
      print('\n<해외유입 환자현황(신규, 누계, 비율)>\n')
    if(n % 3 == 0):
      print(country[c], ':', statistics[n], statistics[n+1], statistics[n+2])
      c = c + 1
  
  n = n + 1