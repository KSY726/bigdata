# 만약 배민에서 음식을 고를려고 하는데
# 선택하기 힘들어 메뉴 추천 기능을 이용
# 치킨, 피자, 분식, 중식
# 랜덤 모듈

import random
print(random.random())


menu = '치킨', '피자', '분식', '중식'
print(random.choice(menu))


import requests.get(https://www.melon.com/)
from bs4 import BeautifulSoup
BeautifulSoup(data.text, 'html.parser')

import requests
from bs4 import BeautifulSoup
 
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/',headers=headers)
 
soup = BeautifulSoup(data.text, 'html.parser')