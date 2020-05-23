import requests
import csv
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTP GET Request
req = requests.get('https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# data = []
# ranking_total = soup.find('#regularTeamRecordList_table')
# ranking_total = soup.find_one('#regularTeamRecordList_table')

# 테이블 가져오기
ranking_total = soup.select('#regularTeamRecordList_table')
print(ranking_total)


# # The main comparison table is currently the first table on the page
# table = bsObj.findAll("table", {"class": "wikitable"})[0]
# rows = ranking_total.find_all('tr')

# csvFile = open("ranking.csv", 'wt', newline='', encoding='utf-8')
# writer = csv.writer(csvFile)

# 테이블 정보를 텍스트로 가져오기
# for ranking in ranking_total:
#     print(ranking.text)

# rows = ranking_total.get('tr')
#
# for row in rows:
#     print(rows)

# data = {}
#
# for ranking in ranking_total:
#     data[ranking.text] = ranking.get('td')
#     print(data)
#
# #json 으로 저장
# with open(os.path.join(BASE_DIR, 'record.json'), 'w+', encoding='utf-8') as json_file: # 인코딩 설정
#     json.dump(data, json_file, ensure_ascii=False)


# try:
#     for ranking in ranking_total:
#         csvRow = []
#         for cell in ranking_total.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
# finally:
#     csvFile.close()
#
# print(ranking)
#
#


