from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote_plus

""" 네이버 블로그 검색결과 """

baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어 입력 : ')

url = baseUrl + quote_plus(plusUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title') # 클래스명이 sh_blog_title인 것들을 모두 찾아 title에 저장

print()

for i in title:
  print("Title -", i.attrs['title']) # attrs : 속성 찾기
  print("Link -", i.attrs['href'], "\n")