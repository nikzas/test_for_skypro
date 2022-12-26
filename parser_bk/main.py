

import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from lxml import html


#https://1wtuer.top/casino/play/1play_1play_luckyjet

html1 = requests.get('http://www.google.com')
#soup = BeautifulSoup(html1, 'html.parser')
#find_text = soup.find('body', {'class': 'webp'})
print(html1.content)








