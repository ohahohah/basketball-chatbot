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

# 테이블 가져오기
# select 는 여러 개의 인스턴스를 찾아 목록을 반환하고 find 는 첫 번째를 찾음. select_one 은 find 와 같다.
# find, find_all, select, select_one 비교
# 근데 find_all 하고 findAll 은 또 뭐가 다를까

# table = soup.find('#regularTeamRecordList_table')
# print(table)
# 결과값이 NONE

# table = soup.find_all('#regularTeamRecordList_table')
# print(table)
# 결과값이 빈 리스트

table = soup.select('#regularTeamRecordList_table')
# print(table)
# 결과값이 html 형식. text만 추출하고 싶은데...

# table = soup.select_one('#regularTeamRecordList_table')
# print(table)
# select와 같은 결과. 왜 똑같지? select_one과 find가 같다고 했는데...

csvFile = open("wkblranking.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in table:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
