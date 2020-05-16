import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

row_select = soup.select('#regularTeamRecordList_table > tr')

result = {}

for row in row_select:
    rank = row.select_one('th > strong').getText()
    team = row.select_one('td[class="tm"] > div > span').getText()
    result[rank] = team

print(result)

# json 으로 저장
with open(os.path.join(BASE_DIR, 'ranking.json'), 'w+', encoding='utf-8') as json_file:  # 인코딩 설정
    json.dump(result, json_file, ensure_ascii=False)
