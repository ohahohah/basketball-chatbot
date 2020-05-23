import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# thead = soup.select_one('thead').getText()
#
# for table_head in thead:
#     print(table_head)
# 왜 한 글자씩 가져오지?


row_select = soup.select('#regularTeamRecordList_table > tr')

ranking_list = {}
gamenumber_list = {}
winningrate_list = {}
win_list = {}
loose_list = {}
gap_lsit = {}
score_list = {}
assist_list = {}
rebound_list = {}
steal_list = {}
block_list = {}
point_list = {}
freethrow_list = {}

for row in row_select:
    team_name = row.select_one('td[class="tm"] > div > span').getText()
    ranking = row.select_one('th > strong').getText()
    # for data in row.select('td'): # 반복부분을 for 문으로 바꿀 수 있을까?
    gamenumber = row.select('td')[1].getText()
    winningrate = row.select('td')[2].getText()
    win = row.select('td')[3].getText()
    loose = row.select('td')[4].getText()
    gap = row.select('td')[5].getText()
    score = row.select('td')[6].getText()
    assist = row.select('td')[7].getText()
    rebound = row.select('td')[8].getText()
    steal = row.select('td')[9].getText()
    block = row.select('td')[10].getText()
    point = row.select('td')[11].getText()
    freethrow = row.select('td')[12].getText()

    ranking_list[team_name] = ranking
    gamenumber_list[team_name] = gamenumber
    winningrate_list[team_name] = winningrate
    win_list[team_name] = win
    loose_list[team_name] = loose
    gap_lsit[team_name] = gap
    score_list[team_name] = score
    assist_list[team_name] = assist
    rebound_list[team_name] = rebound
    steal_list[team_name] = steal
    block_list[team_name] = block
    point_list[team_name] = point
    freethrow_list[team_name] = freethrow

# print(ranking_list)
# print(gamenumber_list)
# print(winningrate_list)
# print(win_list)
# print(loose_list)
# print(gap_lsit)
# print(score_list)
# print(assist_list)
# print(rebound_list)
# print(steal_list)
# print(block_list)
# print(point_list)
# print(freethrow_list)

record = [ranking_list, gamenumber_list, winningrate_list, win_list, loose_list, gap_lsit, score_list, assist_list,
          rebound_list, steal_list, block_list, point_list, freethrow_list]

# json 으로 저장
with open(os.path.join(BASE_DIR, 'record.json'), 'w+', encoding='utf-8') as json_file:  # 인코딩 설정
    json.dump(record, json_file, ensure_ascii=False)

# json 안에 들어가는 dict에 이름을 줄 수 있을까?
