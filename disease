from bs4 import BeautifulSoup
from urllib.request import urlopen

""" 감염병포탈 """

response = urlopen('http://www.cdc.go.kr/npt/biz/npp/portal/nppLwcrIcdMain.do')
soup = BeautifulSoup(response, 'html.parser')

for anchor in soup.select("td.L > a.btn-list"):
  print(anchor.get_text())