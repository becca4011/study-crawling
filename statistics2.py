from bs4 import BeautifulSoup
import urllib.request

""" 코로나 국내 현황 """

url = 'https://google.com/covid19-map/?hl=ko'

header = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html = urllib.request.urlopen(header).read()
soup = BeautifulSoup(html, 'html.parser')

title = []
country = []

for statistics in soup.select('table.SAGQRd > thead > tr.A5V3jc > th.aiByXc'):
  title.append(statistics.get_text())

for statistics in soup.select('table.SAGQRd > tbody.qEfTDe > tr.A5V3jc > td.uMsnNd'):
  country.append(statistics.get_text())

# {:길이} : 문자열 - 왼쪽 / 숫자 - 오른쪽 정렬
# {:<길이} : 왼쪽 정렬
# {:>길이} : 오른쪽 정렬
# {:^길이} : 가운데 정렬

print('{:15}'.format(title[0]), '{:15}'.format(title[1]), '{:^15}'.format(title[2]), '{:^15}'.format(title[3]), '{:^15}'.format(title[4]))

print('------------------------------------------------------------------------------------------------------')

i = 0

while(i < len(country)):
  
  if(i % 5 == 0):
    print('{:7}'.format(country[i]), '{:^20}'.format(country[i + 1]), '{:^33}'.format(country[i + 2]), '{:^10}'.format(country[i + 3]), '{:^25}'.format(country[i + 4]))
  
  i = i + 1