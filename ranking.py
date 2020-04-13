from bs4 import BeautifulSoup
from urllib.request import urlopen

""" 질병관리본부 검색어순위 """

response = urlopen('http://www.cdc.go.kr/')
soup = BeautifulSoup(response, 'html.parser')

i = 1

for anchor in soup.select("ol.slider5"):
  print(anchor.get_text())