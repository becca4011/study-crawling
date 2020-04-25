""" 코로나 정보 """

from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('http://ncov.mohw.go.kr/baroView.do?brdId=4&brdGubun=41')
soup = BeautifulSoup(html, 'html.parser')

n = 0

for i in soup.select('div > div.data_table > table > tbody > tr'):
  if n < 11: # 아래 표도 같이 나와서 조건 지정
    print('<', i.select_one('th').text, '>')

    if n == 0 or n == 2 or n == 4 or n == 6:
      print(i.select_one('td.ta_l').text, '\n')
    else:
      print(i.select_one('td.ta_l > ul > li').text, '\n')

    n = n + 1