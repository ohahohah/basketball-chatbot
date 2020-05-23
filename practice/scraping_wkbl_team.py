import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

head = soup.select_one('thead').get_text()
print(head)
print(type(head))
# head는 team(i) dict에 key로 활용
# 현재 head는 list가 아닌 것 같다. type 확인시 출력이 1번만 된다.


team1 = {}
team2 = {}
team3 = {}
team4 = {}
team5 = {}
team6 = {}
# team_ 뒤에 숫자 반복문 처리가 가능할까?


# 직접 구분해서 작성하면 이렇게 될 것 같은데
row00 = soup.select('#regularTeamRecordList_table > tr')[0].get_text()
row01 = soup.select('#regularTeamRecordList_table > tr')[1].get_text()
row02 = soup.select('#regularTeamRecordList_table > tr')[2].get_text()
row03 = soup.select('#regularTeamRecordList_table > tr')[3].get_text()
row04 = soup.select('#regularTeamRecordList_table > tr')[4].get_text()
row05 = soup.select('#regularTeamRecordList_table > tr')[5].get_text()
print(type(row00))


team1[head] = row00
team2[head] = row01
team3[head] = row02
team4[head] = row03
team5[head] = row04
team6[head] = row05

print(team1)
print(team2)
print(team3)
print(team4)
print(team5)
print(team6)
# dict에 들어가기는 하는데 한 행의 데이터가 통으로 들어감.


# # 반복문으로 해보자
# team1_record = []

# 딕셔너리에 이름을 주고 싶은데
# teams = [team1, team2, team3, team4, team5, team6]

# 반복문을 이용해 보자
# for rows in soup.select('#regularTeamRecordList_table > tr'):
#     # print(rows)
#     for team_name in rows.select('td[class="tm"] > div > span'):
#         team1_record.append(team_name.get_text())
#     for team_name in rows.select('th > strong'):
#         team1_record.append(team_name.get_text())
#     for cell in rows.select('td > span'):
#         team1_record.append(cell.get_text())
#     print(team1)

# 구문이 출력되는 것은 확인 했음. 그런데 row별로 나눠지지가 않음. head 부분에 dict 형태로 넣는 것도 안됨.
# 그래서 이걸 가지고 변형 할 수 있을까 아래에 다시 해보자.

# # team(i) 를 사용 할 수 있을까? i = i + 1
# for rows in soup.select('#regularTeamRecordList_table > tr'):
#     for i, team in range(1, 6):
#         for team_name in rows.select('td[class="tm"] > div > span'):
#             team(i)_record.append(team_name.get_text())
#         for team_name in rows.select('th > strong'):
#             team(i)_record.append(team_name.get_text())
#         for cell in rows.select('td'):
#             team(i)_record.append(cell.get_text())
#             print(team(i)_record)
# 안되네...


# # json 으로 저장
# with open(os.path.join(BASE_DIR, 'wkbl_team.json'), 'w+', encoding='utf-8') as json_file:  # 인코딩 설정
#     json.dump(teams, json_file, ensure_ascii=False)
# # JSONArray?
