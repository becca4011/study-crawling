""" 검사현황 """

from bs4 import BeautifulSoup
import urllib.request

url = 'http://ncov.mohw.go.kr/'

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

num = 1

for i in soup.select('div.info_core > ul.suminfo > li'):
  if num < 4:
    print(i.select_one('span.tit').get_text(), end = ' : ')
    print(i.select_one('span.num').get_text())
  
  num += 1

print()

for j in soup.select('div.chart_d > div.c_chart.c_chart_is > div.cc_figure > p'):
  print(j.select_one('span.num_tit').get_text(), end = ' : ')
  print(j.select_one('span.num_rnum').get_text(), end = ' / ')
  print(j.select_one('span.num_percentage').get_text())