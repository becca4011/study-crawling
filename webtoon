from bs4 import BeautifulSoup
from urllib.request import urlopen

""" 네이버 웹툰 제목 """

response = urlopen('https://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(response, 'html.parser')

for anchor in soup.select("a.title"):
  print(anchor.get_text())