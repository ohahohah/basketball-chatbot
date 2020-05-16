import requests
from bs4 import BeautifulSoup

req = requests.get('https://sports.news.naver.com/basketball/record/index.nhn?category=wkbl')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

#### Using find function
table_find = soup.find(id='regularTeamRecordList_table')
# print(table)

rows_find = table_find.find_all('tr')
# print(rows_find)
# rows2 = soup.find(id='regularTeamRecordList_table').find_all('tr')
# print(rows2)

result_find = {}

for row in rows_find:
    rank = row.find('th').find('strong').getText()
    # print(rank)
    team = row.find('span').getText()
    # print(team)
    # print('-------')

    result_find[rank] = team

# print(result_find)

#### Using select
row_select = soup.select('#regularTeamRecordList_table > tr')
# print(row_select)

result_select = {}

for row in row_select:
    rank = row.select_one('th > strong').getText()
    # print(rank)
    team = row.select_one('span').getText()
    # print(team)
    # print('-------')

    result_select[rank] = team

# print(result_select)
