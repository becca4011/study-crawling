""" 국민안심병원 """

from bs4 import BeautifulSoup
import urllib.request

city = input('지역 입력 : ')

html = urllib.request.urlopen('https://www.mohw.go.kr/react/popup_200128.html').read()
soup = BeautifulSoup(html, 'html.parser')

hos = []
n = 0

for i in soup.select('table.tb_base.safelist.corona > tbody.tb_center > tr > td'):
  hos.append(i.get_text())

print()

while(n < len(hos)):
  if hos[n] == city:
    print(hos[n + 1], hos[n + 2], hos[n + 3], hos[n + 4])

  n = n + 1