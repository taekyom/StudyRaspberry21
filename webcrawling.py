#웹 크롤링(원하는 정보를 긁어오는 것)
from bs4 import BeautifulSoup as bs
from pprint import pprint 
import requests as req

url = 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
html = req.get(url)
#pprint(html.text) #출력
soup = bs(html.text, 'html.parser')

datas = soup.find('div', {'class' : 'detail_box'})
#pprint(finedust)
details = datas.findAll('dd')
#pprint(details)

finedust = details[0].find('span', {'class', 'num'}).get_text() #.get_text() : span태그 없이 원하는 수치(값)만 가져오는 것
#pprint(finedust)
ultrafinedust = details[1].find('span', {'class', 'num'}).get_text()
ozone = details[2].find('span', {'class', 'num'}).get_text()
pprint('{0}, {1}, {2}'.format(finedust, ultrafinedust, ozone))