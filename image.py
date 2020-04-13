from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


""" 이미지 크롤링 """

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어 입력 : ')

url = baseUrl + quote_plus(plusUrl) # 아스키코드로 바뀌어야 검색 가능

html = urlopen(url).read() # html 가져오기
soup = BeautifulSoup(html, 'html.parser') # 가져온 html 분석

img = soup.find_all(class_='_img')

n = 1

for i in img:
  imgUrl = i['data-source'] # 사진 주소

  with urlopen(imgUrl) as f:
    with open('./crawling/' + plusUrl + str(n) + '.jpg', 'wb') as h: # 이미지 저장 경로, 이름
      img = f.read()
      h.write(img)

  n += 1
  print(imgUrl)

print('다운로드 완료')