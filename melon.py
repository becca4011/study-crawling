""" 멜론 차트 """

from bs4 import BeautifulSoup
import urllib.request

header = {'User-Agent' : 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/index.htm'

req = urllib.request.Request(url, headers=header) # 406 error로 사용
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

lst = soup.select('.lst50, .lst100') 
# class를 .으로 나타냄
# 1~100위까지 가져옴
# 멜론 사이트에서, 실제 html은 페이지 2개가 아닌 1개로 이루어져 있음. 그래서 위처럼 하는 것이 가능

for i in lst:
  print(i.select_one('.rank').text, end='위 ') # 순위
  print(i.select_one('.ellipsis.rank01').a.text, end=' ') # 노래 제목
  print(i.select_one('.ellipsis.rank02').a.text, end=' ') # 가수
  print(i.select_one('.ellipsis.rank03').a.text) # 앨범
  # a.text : a 태그 안의 text를 가져옴
  # class 2개일 때는 .ellipsis.rank01 처럼 . 2개를 사용