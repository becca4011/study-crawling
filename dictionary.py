""" 네이버 사전 """

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote_plus

baseUrl1 = 'https://terms.naver.com/search.nhn?query='
baseUrl2 = '&searchType=&dicType=&subject='
plusUrl = input('검색어 입력 : ')

url = baseUrl1 + quote_plus(plusUrl) + baseUrl2

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = []
description = []

for anchor in soup.select('div.subject > strong.title > a'):
  title.append(anchor.get_text())

for anchor in soup.select('div.info_area > p.desc'):
  description.append(anchor.get_text())

i = 0

while(i < len(title)):
  print('\n', title[i], ':\n', description[i], '\n')
  
  i = i + 1

"""
하나만 출력
title = soup.select_one('div.subject > strong.title > a')
description = soup.select_one('div.info_area > p.desc')

print('\n', title.get_text(), '\n', description.get_text(), '\n')
"""