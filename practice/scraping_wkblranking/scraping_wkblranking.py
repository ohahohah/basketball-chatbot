# 웹페이지 요청을 위한 패키지
import requests
# 웹페이지 파싱을 위한 패키지
from bs4 import BeautifulSoup
import csv

# wkbl 순위 페이지 가져오기
req = requests.get('https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl')
# HTML 소스 가져오기
html = req.text
# BeautifulSoup으로 html소스를 python객체로 변환하기
soup = BeautifulSoup(html, 'html.parser')

# 여기까지는 Fix

# 테이블 가져오기
table = soup.find(id='regularTeamRecordList_table')
table_csv = soup.select('#regularTeamRecordList_table')
# print(tables)


# 내용을 행별로 row로 구분
row = table.find_all('tr')
# print(row)

# row 내용을 cell로 받기
for cell in row:
    ranking_team = []
    result_team = []
    for ranking in cell.find_all('th'):
        ranking_team.append(ranking.get_text())
    for result in cell.find_all('td'):
        result_team.append(result.get_text())
    print(ranking_team, result_team)
    print(ranking_team, result_team[0])
# th, td를 따로 가져오는 것은 의미가 없나?

# csv 파일로 저장
csvFile = open("wkblranking.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row_csv in table_csv:
        csvRow = []
        for cell in row_csv.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

# print 되게 작성한 부분과 csv로 작성된 부분을 하나로 합칠 수 있을까?
# print는 find로 가져와서 test 형식으로 가능한데, csv는 select로 가져와야 가능하던데...
# print와 csv로 나누는 건 의미가 없나? csv로 저장만 하면 되려나?

# csv 파일의 행 바꿈은 어떻게 할 수 있을까?
# 기록을 딕셔너리로 넣을 수 있을까?
# 쳇봇에게 csv가 좋을까? 딕셔너리가 좋을까?
