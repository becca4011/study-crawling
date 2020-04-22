""" 위키백과 """

from bs4 import BeautifulSoup
import requests
from urllib.parse import quote_plus

baseUrl = 'https://ko.wikipedia.org/wiki/'
plusUrl = input('검색어 입력 : ')

url = baseUrl + quote_plus(plusUrl)

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

info = soup.select_one('div.mw-parser-output > p')
print('\n', info.get_text())
print('URL :', url)

"""
for i in soup.select('div.mw-parser-output > p'):
  print(i.get_text()) 전체 내용이 나옴
"""